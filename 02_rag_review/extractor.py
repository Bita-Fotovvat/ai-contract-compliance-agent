"""
extractor.py
------------
This file is responsible for reading a PDF file and extracting its raw text content.

When a user uploads a contract PDF through the Streamlit interface, the file is passed
to this module. PyPDF reads each page of the document and extracts the text from it.
The result is one long string containing all the text in the contract, which is then
passed to the next step in the pipeline.

In V1, this raw text was sent directly to GPT.
In V2 (RAG), this raw text gets chunked and embedded instead.

Library used: pypdf
"""

from pypdf import PdfReader

def extract_text(uploaded_file) -> str:
    reader = PdfReader(uploaded_file)
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())