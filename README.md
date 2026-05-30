# AI Contract Compliance & Risk Review Agent
![Python](https://img.shields.io/badge/Python-3.11-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

An AI-powered contract review project that explores the evolution of document intelligence systems, from direct Large Language Model (LLM) analysis to Retrieval-Augmented Generation (RAG).

The goal is to analyze renovation contracts, validate them against predefined compliance standards, identify missing clauses, assess risk, and generate structured compliance reports.

This repository documents the progression from a simple LLM-based solution to a scalable retrieval-based architecture.

---

## Project Motivation

Contract reviews are time-consuming and often require manually checking whether critical legal, financial, and operational clauses are present.

This project explores how AI can assist with contract review workflows by:

* Reading uploaded contract documents
* Evaluating contracts against compliance standards
* Identifying missing or unclear clauses
* Assessing potential risks
* Generating actionable recommendations
* Producing structured compliance reports

The project is intentionally built in stages to demonstrate the progression from basic LLM applications to modern RAG systems.

---

## Repository Structure

```text
ai-contract-compliance-agent/
│
├── 01_llm_review/
│   ├── app.py
│   ├── extractor.py
│   ├── validator.py
│   ├── standards.py
│   ├── requirements.txt
│   └── README.md
│
├── 02_rag_review/
│   ├── (coming soon)
│   └── README.md
│
└── README.md
```

---

## Project Evolution

### Version 1 — LLM-Powered Contract Review

Architecture:

```text
PDF Contract
      │
      ▼
Text Extraction
      │
      ▼
GPT-4o
      │
      ▼
Structured Compliance Report
```

This version focuses on:

* PDF document processing
* Prompt engineering
* OpenAI API integration
* Structured JSON outputs
* Risk assessment workflows
* Streamlit application development

Key limitation:

* The entire document is sent directly to the LLM.
* No retrieval mechanism exists.
* Not considered a Retrieval-Augmented Generation (RAG) system.

---

### Version 2 — RAG-Based Contract Review (Planned)

Architecture:

```text
PDF Contract
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
Vector Database (ChromaDB)
      │
      ▼
Retriever
      │
      ▼
GPT-4o
      │
      ▼
Compliance Report
```

Additional capabilities:

* Semantic retrieval
* Evidence-based clause extraction
* Vector search
* ChromaDB integration
* Retrieval-Augmented Generation (RAG)
* Scalable contract analysis

---

## Compliance Standards

The initial implementation focuses on renovation contracts and evaluates the presence and quality of important clauses.

Current clause categories include:

### Legal

* Parties Identified
* Signatures
* Insurance
* Permits and Inspections
* Governing Law
* Dispute Resolution
* Termination

### Financial

* Payment Schedule
* Liability Cap

### Operational

* Scope of Work
* Change Orders
* Project Schedule
* Warranty

Each rule contains:

* Clause name
* Clause description
* Risk if missing
* Default risk level
* Evidence requirements
* Category classification

---

## Example Output

```json
{
  "clause": "Payment Schedule",
  "status": "pass",
  "confidence_score": 94,
  "explanation": "The contract defines payment milestones and due dates.",
  "evidence": "Progress Payment 1: $14,550 due upon completion of demolition.",
  "recommendation": null,
  "assessed_risk": "none"
}
```

---

## Skills Demonstrated

### Artificial Intelligence

* Large Language Models (LLMs)
* Prompt Engineering
* Retrieval-Augmented Generation (Planned)
* AI-Assisted Risk Assessment

### Data Processing

* PDF Parsing
* Document Intelligence
* Structured Data Extraction
* JSON-Based Workflows

### Software Development

* Python
* Streamlit
* OpenAI API
* Environment Management
* Modular Application Design

### Future Skills (Version 2)

* Embeddings
* Vector Databases
* ChromaDB
* Semantic Search
* Retrieval Systems

---

## Roadmap

### Phase 1 — LLM Review Agent

* PDF Upload
* Contract Validation
* Risk Assessment
* Compliance Reports

### Phase 2 — Enhanced Document Support

* DOCX Support
* Multiple Contract Types
* Employment Agreements
* Lease Agreements
* Vendor Contracts

### Phase 3 — Backend Services

* FastAPI
* REST API Architecture
* PostgreSQL Persistence

### Phase 4 — RAG Implementation

* Chunking
* Embeddings
* ChromaDB
* Retrieval Layer
* Evidence Citation

### Phase 5 — Analytics & Security

* Authentication
* User Management
* Audit Trail
* Contract Analytics Dashboard

---

## Why This Project Matters

Many organizations review contracts manually, which can be time-consuming and error-prone.

This project demonstrates how AI can assist compliance workflows by combining:

* Document processing
* Risk assessment
* Compliance validation
* Explainable AI outputs

while showcasing the evolution from direct LLM usage to modern retrieval-based architectures.

---

## Author

**Bita Fotovvat**

M.Eng. Systems & Technology (Co-op)
McMaster University

LinkedIn:
https://www.linkedin.com/in/bita-fotovvat

GitHub:
https://github.com/Bita-Fotovvat

---

## License

MIT License
