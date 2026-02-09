# Outsource Partner Scout 🧬

**Powered by Exa AI**

This is a demo application built for the Exa AI Take-home Assignment. It demonstrates how Exa's search and enrichment capabilities can be used to solve a critical problem in the Biotech R&D space: finding and vetting specialized CRO/CDMO partners.

## Problem Statement

Biotech R&D teams face massive risks when selecting outsourced partners (CROs/CDMOs). A wrong choice can lead to months of delay or failed programs. Current methods involve:
- Scattered Google searches
- Outdated directories
- Manual reading of capability decks

## The Solution

**Outsource Partner Scout** uses Exa to:
1.  **Discover** niche vendors based on specific technical capabilities (e.g., "mRNA LNP formulation").
2.  **Enrich** vendor profiles with evidence from their websites, press releases, and news.
3.  **Monitor** for risk signals like leadership changes or regulatory warnings.

## How to Run

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Features

-   **Targeted Search:** Filter by Vendor Type, Modality, Stage, Scope, Quality, and Geography.
-   **Evidence-Based Results:** Vendors are scored based on how well their online footprint matches your requirements.
-   **Deep Dive:** View specific claims and excerpts from vendor websites.
-   **Risk Detection:** (Simulated) Alerts for adverse news or regulatory actions.
-   **Comparison:** Side-by-side view of shortlisted candidates.
-   **Export:** Download your shortlist as CSV or JSON.

## Tech Stack

-   **Frontend:** Streamlit (Python)
-   **Data:** Mocked Exa API (simulating `exa-py` SDK behavior)
-   **Logic:** Pandas for data manipulation

## Note on Data

The data in this demo is **mocked** for demonstration purposes. In a production environment, this would connect to the live Exa API to fetch real-time results from the web.
