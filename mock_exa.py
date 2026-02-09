import random
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

class MockExaClient:
    """
    A mock client that simulates the Exa API for the purpose of this demo.
    It returns realistic CRO/CDMO data based on search queries.
    """

    def __init__(self, api_key: str = "mock-key"):
        self.api_key = api_key
        self._db = self._generate_mock_db()

    def _generate_mock_db(self) -> List[Dict[str, Any]]:
        """Generates a database of mock vendors."""
        vendors = [
            {
                "name": "BioVector Manufacturing",
                "type": "CDMO",
                "modalities": ["Viral Vector", "Gene Therapy"],
                "scope": ["GMP Drug Substance", "Fill Finish", "Process Dev"],
                "quality": ["GMP", "ISO 9001"],
                "geo": "US - East Coast",
                "timeline": "Slot available Q4 2024",
                "url": "https://biovector-mfg.example.com",
                "text": "BioVector Manufacturing specializes in high-titer viral vector production. Our GMP facility in Boston offers end-to-end process development and fill-finish services. We recently expanded our capacity for AAV and Lentivirus vectors.",
                "title": "BioVector Mfg - Viral Vector Services",
                "published_date": "2023-11-15"
            },
            {
                "name": "Global Pharma Services",
                "type": "CRO",
                "modalities": ["Small Molecule", "Peptides"],
                "scope": ["Bioanalytical", "Clinical Ops", "Tox"],
                "quality": ["GLP", "GCP"],
                "geo": "EU - Germany",
                "timeline": "Immediate start",
                "url": "https://global-pharma-services.example.com",
                "text": "Global Pharma Services provides comprehensive bioanalytical and toxicology services for small molecules and peptides. Our GLP-compliant labs in Munich support preclinical through Phase III studies.",
                "title": "Global Pharma Services - Bioanalytical Excellence",
                "published_date": "2024-01-10"
            },
            {
                "name": "Synthetix Biologics",
                "type": "Both",
                "modalities": ["mRNA", "Plasmid DNA", "LNP"],
                "scope": ["Process Dev", "GMP Drug Substance", "Analytical Dev"],
                "quality": ["GMP"],
                "geo": "US - West Coast",
                "timeline": "Limited availability 2024",
                "url": "https://synthetix.example.com/capabilities",
                "text": "Synthetix Biologics is a leader in mRNA and LNP manufacturing. We offer rapid process development and cGMP manufacturing for plasmids and mRNA constructs. Our San Diego facility is fully operational.",
                "title": "Synthetix - mRNA & LNP CDMO",
                "published_date": "2023-09-20"
            },
            {
                "name": "CellCure Labs",
                "type": "CDMO",
                "modalities": ["Cell Therapy", "CAR-T"],
                "scope": ["GMP Drug Product", "Logistics", "QC Release"],
                "quality": ["GMP", "Aseptic"],
                "geo": "US - Midwest",
                "timeline": "Q3 2024",
                "url": "https://cellcure-labs.example.com",
                "text": "CellCure Labs provides dedicated suites for autologous and allogeneic cell therapy manufacturing. Our aseptic processing capabilities and cold chain logistics ensure product integrity.",
                "title": "CellCure Labs - Cell Therapy Manufacturing",
                "published_date": "2024-02-01"
            },
            {
                "name": "OmniTox Research",
                "type": "CRO",
                "modalities": ["Small Molecule", "Biologics"],
                "scope": ["Tox", "Safety Pharm", "Pathology"],
                "quality": ["GLP"],
                "geo": "UK",
                "timeline": "Start within 4 weeks",
                "url": "https://omnitox.example.co.uk",
                "text": "OmniTox Research offers rigorous safety assessment and toxicology services. Our GLP facilities in the UK handle diverse modalities including ADCs and bispecifics.",
                "title": "OmniTox - Safety Assessment",
                "published_date": "2023-12-05"
            },
            {
                "name": "Apex Fill & Finish",
                "type": "CDMO",
                "modalities": ["Small Molecule", "Biologics"],
                "scope": ["Fill Finish", "Packaging", "Sterile"],
                "quality": ["GMP", "Sterile"],
                "geo": "EU - France",
                "timeline": "Q2 2024",
                "url": "https://apex-fill.example.com",
                "text": "Apex specializes in sterile fill-finish for vials and syringes. We support clinical to commercial scale manufacturing with EU GMP and FDA approval.",
                "title": "Apex - Sterile Manufacturing",
                "published_date": "2024-03-12"
            },
            {
                "name": "GeneFlow Systems",
                "type": "CDMO",
                "modalities": ["Plasmid DNA", "Viral Vector"],
                "scope": ["Process Dev", "GMP Drug Substance"],
                "quality": ["GMP", "ISO"],
                "geo": "APAC - Singapore",
                "timeline": "High capacity available",
                "url": "https://geneflow.example.sg",
                "text": "GeneFlow Systems in Singapore offers scalable plasmid DNA and viral vector manufacturing. High capacity bioreactors available for immediate booking.",
                "title": "GeneFlow - Scalable Manufacturing",
                "published_date": "2024-01-25"
            },
            {
                "name": "RapidScale Antibodies",
                "type": "Both",
                "modalities": ["Antibody", "ADC"],
                "scope": ["Cell Line Dev", "Process Dev", "GMP Drug Substance"],
                "quality": ["GMP"],
                "geo": "US - Northeast",
                "timeline": "Q1 2025",
                "url": "https://rapidscale-abs.example.com",
                "text": "RapidScale accelerates antibody development from DNA to GMP. Our proprietary CHO platform delivers high titers. ADC conjugation capabilities on-site.",
                "title": "RapidScale - Antibody CDMO",
                "published_date": "2023-10-30"
            },
            {
                "name": "ClinOps Partners",
                "type": "CRO",
                "modalities": ["All"],
                "scope": ["Clinical Ops", "Regulatory", "Patient Recruitment"],
                "quality": ["GCP"],
                "geo": "Global",
                "timeline": "Immediate",
                "url": "https://clinops-partners.example.com",
                "text": "ClinOps Partners manages global clinical trials with a focus on oncology and rare diseases. End-to-end trial management and regulatory support.",
                "title": "ClinOps Partners - Global CRO",
                "published_date": "2024-02-15"
            },
            {
                "name": "BioAnalysis Pro",
                "type": "CRO",
                "modalities": ["Large Molecule", "Gene Therapy"],
                "scope": ["Bioanalytical", "Immunogenicity", "Biomarkers"],
                "quality": ["GLP", "GCLP"],
                "geo": "US - West Coast",
                "timeline": "2 weeks lead time",
                "url": "https://bioanalysis-pro.example.com",
                "text": "BioAnalysis Pro specializes in large molecule bioanalysis, including ADA and NAb assays. Expert support for gene therapy biodistribution studies.",
                "title": "BioAnalysis Pro - Specialized Assays",
                "published_date": "2023-11-20"
            },
            {
                "name": "OligoTech Manufacturing",
                "type": "CDMO",
                "modalities": ["Oligonucleotide", "siRNA"],
                "scope": ["Process Dev", "GMP Drug Substance", "Analysis"],
                "quality": ["GMP", "ISO 13485"],
                "geo": "US - Midwest",
                "timeline": "Q1 2024",
                "url": "https://oligotech-mfg.example.com",
                "text": "OligoTech is a dedicated CDMO for oligonucleotide therapeutics. We support siRNA, antisense, and aptamer programs from gram to kilogram scale.",
                "title": "OligoTech - Oligonucleotide Specialists",
                "published_date": "2023-12-01"
            },
            {
                "name": "EuroClinical Research",
                "type": "CRO",
                "modalities": ["Small Molecule", "Biologics"],
                "scope": ["Clinical Ops", "Data Management", "Biostats"],
                "quality": ["GCP", "GDPR Compliant"],
                "geo": "EU - All Countries",
                "timeline": "Immediate",
                "url": "https://euroclinical.example.eu",
                "text": "EuroClinical Research provides full-service clinical trial management across Europe. Local experts in every EU member state ensure regulatory compliance and swift recruitment.",
                "title": "EuroClinical - Pan-European CRO",
                "published_date": "2024-01-05"
            },
            {
                "name": "Peptide Synthesis Inc.",
                "type": "CDMO",
                "modalities": ["Peptide"],
                "scope": ["GMP Drug Substance", "Process Dev"],
                "quality": ["GMP"],
                "geo": "US - South",
                "timeline": "Q2 2024",
                "url": "https://peptide-synth.example.com",
                "text": "We synthesize high-purity peptides for clinical and commercial use. Our solid-phase synthesis platform is optimized for complex sequences.",
                "title": "Peptide Synthesis Inc - Peptide CDMO",
                "published_date": "2023-10-10"
            },
            {
                "name": "BioLogic Safety Labs",
                "type": "CRO",
                "modalities": ["Biologics", "Cell Therapy"],
                "scope": ["Tox", "Safety Pharm"],
                "quality": ["GLP"],
                "geo": "APAC - Australia",
                "timeline": "Start within 1 week",
                "url": "https://biologic-safety.example.au",
                "text": "BioLogic Safety Labs in Australia offers expedited toxicology studies. Benefit from the R&D tax incentive while accessing world-class GLP facilities.",
                "title": "BioLogic Safety - Australian Tox Services",
                "published_date": "2024-02-20"
            }
        ]
        return vendors

    def search_and_contents(
        self,
        query: str,
        type: Optional[str] = None,
        num_results: int = 10,
        use_autoprompt: bool = True
    ) -> Dict[str, Any]:
        """
        Simulates the Exa.search_and_contents method.
        Filters the mock database based on the query and type.
        """
        results = []

        # Simple keyword matching for the mock
        query_lower = query.lower()

        for vendor in self._db:
            # Check if vendor matches the "type" filter if provided (CRO/CDMO)
            # In the app, "Both" might be passed, or specific ones.
            # If the vendor is "Both", it matches any request for CRO or CDMO.
            # If the request is for "Both", it matches everything.

            # Since the API doesn't strictly filter by these fields natively (it uses semantic search),
            # we will simulate "relevance" by checking if the query terms appear in the text/modalities.

            score = 0
            searchable_text = (
                f"{vendor['name']} {vendor['type']} "
                f"{' '.join(vendor['modalities'])} {' '.join(vendor['scope'])} "
                f"{vendor['text']} {vendor['geo']}"
            ).lower()

            # Basic keyword scoring
            terms = query_lower.split()
            for term in terms:
                if term in searchable_text:
                    score += 1

            # Boost score if the explicit type matches
            if "cro" in query_lower and (vendor['type'] == "CRO" or vendor['type'] == "Both"):
                score += 2
            if "cdmo" in query_lower and (vendor['type'] == "CDMO" or vendor['type'] == "Both"):
                score += 2

            # Filter out zero scores if query is specific, but allow all if query is generic
            if score > 0 or query == "*":
                # Create a result object structure similar to Exa
                results.append({
                    "id": f"exa-result-{random.randint(1000, 9999)}",
                    "title": vendor["title"],
                    "url": vendor["url"],
                    "publishedDate": vendor["published_date"],
                    "author": None,
                    "score": score + random.random(), # Add noise to score
                    "text": vendor["text"],
                    "highlights": [vendor["text"][:100] + "..."],
                    "highlightScores": [0.9],
                    # We inject the structured data into "metadata" or custom fields for the app to use
                    "custom_metadata": {
                        "vendor_name": vendor["name"],
                        "vendor_type": vendor["type"],
                        "modalities": vendor["modalities"],
                        "scope": vendor["scope"],
                        "quality": vendor["quality"],
                        "geo": vendor["geo"],
                        "timeline": vendor["timeline"]
                    }
                })

        # Sort by score descending
        results.sort(key=lambda x: x["score"], reverse=True)

        return {
            "results": results[:num_results],
            "autopromptString": f"Here is the autoprompt for: {query}"
        }

if __name__ == "__main__":
    # Test the mock client
    client = MockExaClient()
    res = client.search_and_contents("mRNA CDMO GMP")
    print(f"Found {len(res['results'])} results")
    for r in res['results']:
        print(f"- {r['title']} ({r['score']:.2f})")
