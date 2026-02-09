import streamlit as st
import pandas as pd
import json
from mock_exa import MockExaClient

# Page Config
st.set_page_config(
    page_title="Outsource Partner Scout",
    page_icon="🧬",
    layout="wide"
)

# Initialize Client
@st.cache_resource
def get_client():
    return MockExaClient()

client = get_client()

# Header
st.title("🧬 Outsource Partner Scout")
st.markdown("""
**Find the perfect CRO/CDMO partner for your biotech program.**
Powered by Exa AI - Discovery & Enrichment Layer.
""")

# Sidebar - Program Requirements
with st.sidebar:
    st.header("1. Program Requirements")

    vendor_type = st.radio(
        "Vendor Type",
        ["Both", "CRO", "CDMO"],
        help="Select the type of partner you are looking for."
    )

    st.subheader("Modality")
    modalities = st.multiselect(
        "Select Modality(s)",
        ["Small Molecule", "Large Molecule", "Antibody", "ADC", "Peptide",
         "Oligonucleotide", "mRNA", "Viral Vector", "Cell Therapy", "Gene Therapy", "Plasmid DNA"],
        default=[]
    )

    st.subheader("Stage")
    stage = st.selectbox(
        "Development Stage",
        ["Discovery", "Preclinical", "Phase I", "Phase II", "Phase III", "Commercial"]
    )

    st.subheader("Scope of Work")
    scope_options = [
        "Bioanalytical", "Tox", "Safety Pharm", "Clinical Ops", "Regulatory", # CRO
        "Process Dev", "Cell Line Dev", "GMP Drug Substance", "GMP Drug Product",
        "Fill Finish", "QC Release", "Stability", "Logistics" # CDMO
    ]
    scope = st.multiselect("Select Services Needed", scope_options)

    st.subheader("Quality & Compliance")
    quality_reqs = st.multiselect(
        "Quality Standards",
        ["GLP", "GCP", "GMP", "ISO 9001", "ISO 13485", "Aseptic", "Sterile", "Cold Chain"]
    )

    st.subheader("Geography")
    geo_pref = st.selectbox(
        "Preferred Region",
        ["Any", "US - East Coast", "US - West Coast", "US - Midwest", "EU", "APAC", "Global"]
    )

    st.subheader("Timeline")
    timeline = st.text_input("Timeline Requirement", placeholder="e.g. Need slot within 90 days")

    st.markdown("---")
    # Store search inputs in session state to persist across reruns
    if st.button("Find Partners", type="primary"):
        st.session_state.search_triggered = True
        st.session_state.search_query = {
            "vendor_type": vendor_type,
            "modalities": modalities,
            "stage": stage,
            "scope": scope,
            "quality": quality_reqs,
            "geo": geo_pref,
            "timeline": timeline
        }

# Logic Functions

def construct_exa_query(inputs):
    """Constructs a natural language query for Exa based on inputs."""
    query_parts = []

    if inputs["vendor_type"] != "Both":
        query_parts.append(inputs["vendor_type"])

    if inputs["modalities"]:
        query_parts.append(" ".join(inputs["modalities"]))

    if inputs["scope"]:
        query_parts.append(" ".join(inputs["scope"]))

    if inputs["quality"]:
        query_parts.append(" ".join(inputs["quality"]))

    if inputs["geo"] != "Any":
        query_parts.append(inputs["geo"])

    if inputs["timeline"]:
        query_parts.append(inputs["timeline"])

    return " ".join(query_parts)

# Main Area Logic

if st.session_state.get("search_triggered"):
    inputs = st.session_state.search_query

    query = construct_exa_query(inputs)

    with st.spinner(f"Scanning the web for '{query}'..."):
        # Simulated API Call
        response = client.search_and_contents(
            query,
            type=inputs["vendor_type"],
            num_results=10
        )
        results = response["results"]

    if not results:
        st.warning("No partners found matching your specific criteria. Try broadening your search.")
    else:
        # Prepare Data for Display
        data_rows = []
        for r in results:
            meta = r["custom_metadata"]
            data_rows.append({
                "Vendor Name": meta["vendor_name"],
                "Type": meta["vendor_type"],
                "Modality": ", ".join(meta["modalities"]),
                "Scope": ", ".join(meta["scope"]),
                "Quality": ", ".join(meta["quality"]),
                "Location": meta["geo"],
                "Timeline": meta["timeline"],
                "Evidence": r["url"],
                "Highlight": r["highlights"][0],
                "Score": r["score"],
                "Full Text": r["text"],
                "id": r["id"]
            })

        df = pd.DataFrame(data_rows)

        # Tabs for different views
        tab1, tab2, tab3 = st.tabs(["📋 Shortlist", "🔍 Vendor Deep Dive", "⚖️ Compare"])

        with tab1:
            st.subheader(f"Found {len(results)} Potential Partners")
            st.dataframe(
                df[["Vendor Name", "Type", "Modality", "Scope", "Quality", "Location", "Timeline"]],
                use_container_width=True,
                hide_index=True
            )

            # Export Buttons
            c1, c2 = st.columns([1, 10])
            with c1:
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name='vendor_shortlist.csv',
                    mime='text/csv',
                )
            with c2:
                json_str = df.to_json(orient="records")
                st.download_button(
                    label="Download JSON",
                    data=json_str,
                    file_name='vendor_shortlist.json',
                    mime='application/json',
                )

        with tab2:
            st.subheader("Vendor Evidence Brief")
            selected_vendor_name = st.selectbox(
                "Select a vendor to inspect:",
                df["Vendor Name"].tolist(),
                key="deep_dive_select"
            )

            if selected_vendor_name:
                selected_row = df[df["Vendor Name"] == selected_vendor_name].iloc[0]

                # Header
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"## {selected_row['Vendor Name']}")
                    st.caption(f"**{selected_row['Type']}** | {selected_row['Location']}")
                with c2:
                    st.metric("Fit Score", f"{selected_row['Score']:.1f}/5.0")

                st.markdown("---")

                # Claims vs Requirements
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("#### ✅ Capability Match")
                    # Logic to check matches
                    matched_modalities = [m for m in inputs["modalities"] if m in selected_row["Modality"]]
                    matched_scope = [s for s in inputs["scope"] if s in selected_row["Scope"]]
                    matched_quality = [q for q in inputs["quality"] if q in selected_row["Quality"]]

                    if matched_modalities:
                        st.success(f"**Modalities:** {', '.join(matched_modalities)}")
                    if matched_scope:
                        st.success(f"**Services:** {', '.join(matched_scope)}")
                    if matched_quality:
                        st.success(f"**Quality:** {', '.join(matched_quality)}")

                    if not (matched_modalities or matched_scope or matched_quality):
                        st.info("No direct keyword match on selected criteria, but contextually relevant.")

                with c2:
                    st.markdown("#### ⚠️ Risk Signals")
                    if selected_row['Score'] < 4.0:
                        st.warning("Low relevance score suggests potential capability gap or outdated info.")
                        # Random risk signal for demo
                        st.error("Recent facility warning letter (simulated)")
                    else:
                        st.success("No adverse regulatory actions found in last 12 months.")

                st.markdown("#### 📄 Exa Evidence Source")
                st.info(f"**Excerpt:** \"{selected_row['Highlight']}\"")
                st.markdown(f"**Source URL:** [{selected_row['Evidence']}]({selected_row['Evidence']})")

                with st.expander("View Full Extracted Text"):
                    st.write(selected_row["Full Text"])

        with tab3:
            st.subheader("Side-by-Side Comparison")

            compare_vendors = st.multiselect(
                "Select vendors to compare (max 4):",
                df["Vendor Name"].tolist(),
                default=df["Vendor Name"].tolist()[:2],
                max_selections=4
            )

            if compare_vendors:
                # Filter dataframe
                comp_df = df[df["Vendor Name"].isin(compare_vendors)].set_index("Vendor Name")
                # Transpose for comparison
                comp_df_t = comp_df[["Type", "Modality", "Scope", "Quality", "Location", "Timeline", "Score"]].transpose()
                st.dataframe(comp_df_t, use_container_width=True)
            else:
                st.info("Select at least one vendor to compare.")

else:
    st.info("👈 Please define your program requirements in the sidebar and click **Find Partners**.")

    st.subheader("How it works")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 1. Define")
        st.caption("Input your specific modality, stage, and service needs.")
    with c2:
        st.markdown("#### 2. Discover")
        st.caption("Exa scans thousands of vendor sites, news, and reports.")
    with c3:
        st.markdown("#### 3. Select")
        st.caption("Compare verified capabilities and risk signals side-by-side.")
