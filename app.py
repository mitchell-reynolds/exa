import re

import streamlit as st
import pandas as pd
import os
from exa_py import Exa
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Config & Initialization
# ---------------------------------------------------------------------------
load_dotenv()

st.set_page_config(
    page_title="Exa AI — Biotech Research",
    page_icon="🧬",
    layout="wide",
)


def get_exa_client(api_key: str):
    """Return an Exa client for the given API key, or None if the key is empty."""
    if not api_key or not api_key.strip():
        return None
    try:
        return Exa(api_key.strip())
    except Exception as e:
        st.error(f"Failed to initialize Exa client: {e}")
        return None

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("🧬 Exa AI — Biotech Research Assistant")
st.markdown(
    "Enter a research question below and get an **executive summary** "
    "plus a **ranked table** of the most relevant sources across papers, "
    "news, social media, and more."
)

# ---------------------------------------------------------------------------
# Sidebar — Query Controls
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("🔑 API Key")
    user_api_key = st.text_input(
        "Exa API Key",
        type="password",
        placeholder="Paste your Exa API key here",
        help="Enter your Exa API key. This overrides any key set in `.env`.",
    )

    # Resolve the key: sidebar input takes priority, then .env
    resolved_key = user_api_key.strip() if user_api_key else os.getenv("EXA_API_KEY", "")

    st.markdown("---")
    st.header("🔬 Research Query")

    query = st.text_area(
        "What are you researching?",
        placeholder="e.g. Latest mRNA vaccine delivery platform innovations",
        height=120,
    )

    st.markdown("---")
    st.subheader("Filters")

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Published after", value=None)
    with col2:
        end_date = st.date_input("Published before", value=None)

    num_results = st.slider(
        "Results per category",
        min_value=3,
        max_value=15,
        value=5,
        help="Number of results to retrieve per source category "
        "(paper, news, tweet, general). Total results will be up to 4× this.",
    )

    st.markdown("---")
    search_clicked = st.button("🔍 Search", type="primary", width="stretch")

# ---------------------------------------------------------------------------
# Exa Client Initialization
# ---------------------------------------------------------------------------
exa = get_exa_client(resolved_key)

if search_clicked and not exa:
    st.error(
        "**Exa API key is required.** "
        "Please enter your API key in the sidebar, or set `EXA_API_KEY` in a `.env` file.\n\n"
        "```\nEXA_API_KEY=your_key_here\n```"
    )
    st.stop()

# ---------------------------------------------------------------------------
# Search helpers
# ---------------------------------------------------------------------------

# Category passes: (label, category kwarg, search type)
SEARCH_PASSES = [
    ("Paper", "research paper", "auto"),
    ("News", "news", "auto"),
    ("Tweet", "tweet", "auto"),
    ("Other", None, "auto"),  # catch-all for conferences, blogs, transcripts, etc.
]


def _clean_text(raw: str) -> str:
    """Strip web-scraping noise from Exa extracted text."""
    if not raw:
        return ""
    # Remove markdown images / broken image refs  e.g. ![alt](url), [![...]], ![]
    text = re.sub(r"!\[[^\]]*\](?:\([^)]*\))?", "", raw)
    # Remove standalone markdown link brackets used as nav items  e.g. [Dashboard]
    text = re.sub(r"^\s*\[[^\]]{1,40}\]\s*$", "", text, flags=re.MULTILINE)
    # Remove common boilerplate lines
    boilerplate = [
        "Skip to main content", "Skip to article", "Skip to navigation",
        "An official website of the United States government",
        "Here's how you know", "Official websites use .gov",
        "Secure .gov websites use HTTPS", "NCBI home page",
        "Log out", "Search NCBI", "Search PMC",
        "BMC journals have moved to Springer Nature Link",
    ]
    for phrase in boilerplate:
        text = text.replace(phrase, "")
    # Collapse excessive whitespace / blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def _build_date_kwargs(start, end):
    """Convert optional date inputs to ISO strings for the Exa API."""
    kwargs = {}
    if start:
        kwargs["start_published_date"] = start.isoformat() + "T00:00:00.000Z"
    if end:
        kwargs["end_published_date"] = end.isoformat() + "T23:59:59.000Z"
    return kwargs


def run_multi_pass_search(query_text, n_per_pass, start, end):
    """Execute 4 category-specific searches and return combined, deduplicated rows."""
    date_kwargs = _build_date_kwargs(start, end)
    all_rows = []
    seen_urls = set()

    for label, category, search_type in SEARCH_PASSES:
        try:
            kwargs = dict(
                query=query_text,
                type=search_type,
                num_results=n_per_pass,
                contents={"text": True},
                **date_kwargs,
            )
            if category is not None:
                kwargs["category"] = category

            response = exa.search(**kwargs)

            for r in response.results:
                url = getattr(r, "url", None) or ""
                if url in seen_urls:
                    continue
                seen_urls.add(url)

                raw_text = getattr(r, "text", "") or ""
                text = _clean_text(raw_text)
                summary = text[:300].strip()
                if len(text) > 300:
                    summary += "…"

                all_rows.append(
                    {
                        "Title": getattr(r, "title", "Untitled") or "Untitled",
                        "URL": url,
                        "Category": label,
                        "Published": getattr(r, "published_date", None) or "",
                        "Author": getattr(r, "author", None) or "",
                        "Summary": summary,
                        "_full_text": text,
                    }
                )
        except Exception as e:
            # Silently skip a failing category pass so other passes still return
            st.toast(f"⚠️ {label} search encountered an issue: {e}", icon="⚠️")

    return all_rows


# ---------------------------------------------------------------------------
# Main Area — Results
# ---------------------------------------------------------------------------

if search_clicked and query:
    # Store in session state so results persist across reruns
    st.session_state["query"] = query
    st.session_state["search_triggered"] = True
    st.session_state["start_date"] = start_date
    st.session_state["end_date"] = end_date
    st.session_state["num_results"] = num_results
elif search_clicked and not query:
    st.warning("Please enter a research question in the sidebar.")

if st.session_state.get("search_triggered"):
    q = st.session_state["query"]

    # ------------------------------------------------------------------
    # Section A — Executive Summary (streamed)
    # ------------------------------------------------------------------
    st.header("📝 Executive Summary")
    summary_container = st.container()
    with summary_container:
        try:
            _summary_parts = []

            def _text_chunks(stream):
                """Yield only the readable text from stream_answer chunks."""
                for chunk in stream:
                    if isinstance(chunk, str):
                        _summary_parts.append(chunk)
                        yield chunk
                    elif hasattr(chunk, "content") and chunk.content:
                        _summary_parts.append(chunk.content)
                        yield chunk.content
                    elif hasattr(chunk, "text") and chunk.text:
                        _summary_parts.append(chunk.text)
                        yield chunk.text

            stream = exa.stream_answer(q, text=True)
            st.write_stream(_text_chunks(stream))
            st.session_state["exec_summary"] = "".join(_summary_parts)
        except Exception as e:
            st.error(f"Could not generate executive summary: {e}")

    st.markdown("---")

    # ------------------------------------------------------------------
    # Section B — Ranked Results Table (multi-pass)
    # ------------------------------------------------------------------
    st.header("📊 Source Results")

    with st.spinner("Searching across papers, news, tweets, and more…"):
        rows = run_multi_pass_search(
            q,
            st.session_state["num_results"],
            st.session_state.get("start_date"),
            st.session_state.get("end_date"),
        )

    if not rows:
        st.warning(
            "No results found. Try broadening your query or adjusting the date range."
        )
    else:
        df = pd.DataFrame(rows)

        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Sources", len(df))
        col2.metric("Papers", len(df[df["Category"] == "Paper"]))
        col3.metric("News", len(df[df["Category"] == "News"]))
        col4.metric("Tweets + Other", len(df[df["Category"].isin(["Tweet", "Other"])]))

        # Interactive table
        st.dataframe(
            df[["Title", "URL", "Category", "Published", "Author", "Summary"]],
            column_config={
                "URL": st.column_config.LinkColumn("URL", display_text="Open"),
            },
            width="stretch",
            hide_index=True,
        )

        # Expandable full-text previews
        st.subheader("🔎 Full Text Previews")
        for _, row in df.iterrows():
            with st.expander(f"[{row['Category']}] {row['Title']}"):
                st.caption(f"Source: {row['URL']}")
                if row["Author"]:
                    st.caption(f"Author: {row['Author']}")
                st.text(row["_full_text"][:2000] if row["_full_text"] else "No text available.")

        # --------------------------------------------------------------
        # Section C — Deep Dive (follow-up refinement)
        # --------------------------------------------------------------
        st.markdown("---")
        st.header("🔬 Deep Dive")
        st.caption(
            "Generate a deeper analysis based on the executive summary above, "
            "plus discover related sources via semantic similarity."
        )

        if st.button("🔬 Generate Deep Dive", type="secondary", width="stretch"):
            exec_summary = st.session_state.get("exec_summary", "")

            if not exec_summary:
                st.warning("No executive summary available to refine. Please run a search first.")
            else:
                # -- Deep Dive Summary --
                st.subheader("📖 Deeper Analysis")
                refined_prompt = (
                    f'Based on this research summary about "{q}":\n\n'
                    f"{exec_summary}\n\n"
                    "Provide a deeper analysis covering:\n"
                    "- Key gaps or unanswered questions in the current research\n"
                    "- Emerging trends or breakthroughs that may be underreported\n"
                    "- Contrarian or alternative viewpoints\n"
                    "- Specific recent developments (conferences, preprints, clinical trials) not covered above"
                )
                try:
                    deep_parts = []

                    def _deep_chunks(stream):
                        for chunk in stream:
                            if isinstance(chunk, str):
                                deep_parts.append(chunk)
                                yield chunk
                            elif hasattr(chunk, "content") and chunk.content:
                                deep_parts.append(chunk.content)
                                yield chunk.content
                            elif hasattr(chunk, "text") and chunk.text:
                                deep_parts.append(chunk.text)
                                yield chunk.text

                    deep_stream = exa.stream_answer(refined_prompt, text=True)
                    st.write_stream(_deep_chunks(deep_stream))
                except Exception as e:
                    st.error(f"Deep dive analysis failed: {e}")

                # -- Related Sources via find_similar --
                st.subheader("🔗 Related Sources")
                top_url = df.iloc[0]["URL"] if len(df) > 0 else None
                if top_url:
                    try:
                        with st.spinner("Finding semantically similar sources…"):
                            similar = exa.find_similar_and_contents(
                                top_url,
                                num_results=5,
                                text=True,
                            )
                        if similar.results:
                            sim_rows = []
                            for r in similar.results:
                                text = getattr(r, "text", "") or ""
                                snippet = text[:200].strip()
                                if len(text) > 200:
                                    snippet += "…"
                                sim_rows.append({
                                    "Title": getattr(r, "title", "Untitled") or "Untitled",
                                    "URL": getattr(r, "url", "") or "",
                                    "Snippet": snippet,
                                })
                            sim_df = pd.DataFrame(sim_rows)
                            st.dataframe(
                                sim_df,
                                column_config={
                                    "URL": st.column_config.LinkColumn("URL", display_text="Open"),
                                },
                                width="stretch",
                                hide_index=True,
                            )
                        else:
                            st.info("No similar sources found.")
                    except Exception as e:
                        st.error(f"Could not find similar sources: {e}")
                else:
                    st.info("No top result URL available for similarity search.")

else:
    # Landing state
    st.info("👈 Enter your research question in the sidebar and click **Search**.")

    st.subheader("How it works")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 1. Ask")
        st.caption("Type any biotech research question in natural language.")
    with c2:
        st.markdown("#### 2. Discover")
        st.caption(
            "Exa searches across research papers, news, tweets, conference talks, and more."
        )
    with c3:
        st.markdown("#### 3. Synthesize")
        st.caption(
            "Get an AI-generated executive summary and a ranked table of sources."
        )
