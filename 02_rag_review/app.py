"""
app.py
------
This file is the entry point of the application. It builds the Streamlit user
interface and orchestrates the entire RAG pipeline from start to finish.

What Streamlit does:
Streamlit is a Python library that turns a regular Python script into an
interactive web application. Every time the user interacts with the UI (uploads
a file, clicks a button), Streamlit re-runs the script from top to bottom.

What this file does step by step:
1. Renders the page layout: title, sidebar, file uploader, and button
2. When the user uploads a PDF and clicks Analyze:
     - Calls extractor.py  → get raw text
     - Calls chunker.py    → split into chunks
     - Calls embedder.py   → embed chunks into ChromaDB
     - Calls validator.py  → retrieve relevant chunks per clause, evaluate with GPT
3. Displays the compliance summary: score, pass/fail/unclear counts
4. Renders each finding in an expandable card showing explanation,
   evidence quote, and recommendation

This file contains no business logic; it only handles the UI and calls the
other modules. Keeping UI and logic separate is good software design practice
and will make it easier to add a FastAPI backend in Phase 3.

Library used: streamlit
"""

import streamlit as st
from extractor import extract_text
from chunker import chunk_text
from embedder import build_vector_store
from validator import validate_contract
from standards import STANDARDS

st.set_page_config(page_title="RAG Contract Compliance Agent", page_icon="", layout="wide")
st.title("RAG Contract Compliance & Risk Review Agent")
st.caption("V2 — Retrieval-Augmented Generation pipeline")

with st.sidebar:
    st.header("Pipeline")
    st.markdown("""
    1. Extract text from PDF
    2. Chunk contract into segments
    3. Embed chunks into ChromaDB
    4. Retrieve relevant sections per clause
    5. GPT evaluates each clause
    6. Generate compliance report
    """)
    st.markdown(f"**Clauses checked:** {len(STANDARDS)}")
    st.markdown("**Model:** GPT-4o + text-embedding-3-small")

uploaded_file = st.file_uploader("Upload a contract (PDF)", type=["pdf"])

if uploaded_file and st.button("Analyze Contract", type="primary"):

    with st.spinner("Step 1/4 — Extracting text..."):
        text = extract_text(uploaded_file)

    with st.spinner("Step 2/4 — Chunking contract..."):
        chunks = chunk_text(text)
        st.sidebar.success(f"Created {len(chunks)} chunks")

    with st.spinner("Step 3/4 — Building vector store..."):
        collection, embeddings_model = build_vector_store(chunks)

    with st.spinner("Step 4/4 — Analyzing clauses with RAG..."):
        results = validate_contract(collection, embeddings_model)

    total = len(results)
    passed = sum(1 for r in results if r["status"] == "pass")
    failed = sum(1 for r in results if r["status"] == "fail")
    unclear = sum(1 for r in results if r["status"] == "unclear")
    score = round((passed / total) * 100) if total else 0

    st.markdown("---")
    st.subheader("Compliance Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Compliance Score", f"{score}%")
    col2.metric("Pass", passed)
    col3.metric("Fail", failed)
    col4.metric("Unclear", unclear)

    st.markdown("---")
    st.subheader("Findings")

    for r in results:
        icon = {"pass": "[PASS]", "fail": "[FAIL]", "unclear": "[UNCLEAR]"}.get(r["status"], "?")
        risk = r.get("assessed_risk", "unknown")
        confidence = r.get("confidence_score", 0)

        with st.expander(f"{icon}  {r['clause']}  |  Risk: {risk.capitalize()}  |  Confidence: {confidence}%"):
            st.write(r.get("explanation", ""))
            if r.get("evidence"):
                st.info(f"Evidence found:\n> {r['evidence']}")
            if r.get("recommendation"):
                st.warning(f"Recommendation: {r['recommendation']}")