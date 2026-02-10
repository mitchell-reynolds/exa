# Exa AI for Biotech Researchers 🧬

**Intelligent Research Assistant Powered by Exa AI + Claude**

An AI-powered research applet that helps biotech researchers discover, synthesize, and understand the latest scientific literature, clinical trials, and industry news. Built with the Exa AI SDK for deep neural search and Claude for intelligent synthesis.

## Problem Statement

Biotech researchers are overwhelmed by the volume of scientific information available today. Manually searching, reading, and synthesizing this information is:

- **Time-consuming**: Hours spent filtering through irrelevant search results
- **Fragmented**: Information is spread across various formats (papers, news, social media)
- **Hard to Synthesize**: Difficult to extract key insights and patterns quickly
- **Resource Intensive**: Requires significant cognitive load to create executive summaries for stakeholders

## The Solution

This research assistant leverages:

1. **Intelligent Search**: Deep neural search via Exa AI to find the most relevant biotech content
2. **Executive Summarization**: Automatically generates comprehensive summaries with clear headings and bullet points
3. **Structured Insights**: Provides a UI-friendly table of ranked results with categories (papers, news, tweets) and generated summaries
4. **Streamlined Workflow**: A simple "query-in, insights-out" interface built with Streamlit

## Use Cases

- **Literature Review**: Quickly synthesize the current state of research for a specific molecule or therapy
- **Competitive Intelligence**: Track news and announcements from competing biotech firms
- **Executive Reporting**: Generate structured summaries for stakeholders based on real-time data
- **Trend Analysis**: Identify emerging topics in the biotech community across various platforms

## How to Run

1. Clone the repository
2. Create and activate the [Conda](https://docs.conda.io/en/latest/) environment:
   ```bash
   conda create -n exa python=3.10 -y
   conda activate exa
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables:
   ```bash
   # Create a .env file with your Exa API key
   echo "EXA_API_KEY=your_api_key_here" > .env
   ```
5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Features

- **Natural Language Queries**: Simply input what you're researching
- **Executive Summaries**: Comprehensive, well-structured summaries with clear headings and bullet points
- **Ranked Results Table**: View relevant information ranked by relevance with:
  - Title
  - URL
  - Category (research paper, news, tweet, etc.)
  - AI-generated summary
- **Multi-Source Intelligence**: Aggregates information from scientific papers, news articles, and social media

## Tech Stack

- **Frontend**: Streamlit (Python)
- **Search Engine**: [Exa AI SDK](https://exa.ai/docs/sdks/python-sdk)
- **AI Synthesis**: Claude Code / Anthropic API
- **Environment**: `.env` for `EXA_API_KEY` management
- **Data Processing**: Pandas for data manipulation

## Project Structure

```
exa/
├── app.py                  # Main Streamlit application
├── memory-bank/            # Project documentation and task tracking
│   ├── docs/              # Core project documentation
│   │   ├── prd.md         # Product Requirements Document
│   │   └── architecture/  # System design and ADRs
│   ├── tasks/             # Task tracking and implementation workspace
│   └── reference/         # Standards, schemas, workflow guidelines
├── CLAUDE.md              # AI assistant guidelines
└── README.md              # This file
```

## Development

This project follows a structured development workflow with clear documentation, task tracking, and quality standards. See `CLAUDE.md` and `memory-bank/reference/WORKFLOW.md` for details.

## Testing Deployment Results for the Streamlit App
Using the following text:
```
Find the foundational research on age related macular degeneration as well as the latest research. I'm particularly interested in the CD59 protein and other areas that might be promising to implement for clinical trials.
```

## Note

This is a demonstration project showcasing how Exa AI's search capabilities can be combined with AI synthesis to solve real problems in biotech research.
