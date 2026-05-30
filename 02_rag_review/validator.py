"""
validator.py
------------
This file is responsible for evaluating each compliance clause using GPT-4o,
based on the chunks retrieved from ChromaDB.

This is the "G" in RAG — the Generation step.

How it works:
For each clause in the standards list, this file:
1. Calls retriever.py to get the most relevant contract chunks
2. Sends those chunks plus the clause definition to GPT-4o
3. Asks GPT to evaluate whether the clause is satisfied
4. Parses the structured JSON response

The key difference from V1:
In V1, GPT received the entire contract text.
In V2, GPT only receives 3 targeted chunks per clause. This makes the evaluation
more precise, reduces token usage (cost), and forces the model to ground its
findings in specific retrieved evidence rather than scanning everything itself.

The system prompt instructs GPT to return a consistent JSON structure so that
the results can be reliably parsed and displayed in the UI.

Libraries used: openai, python-dotenv
"""

import json
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
from standards import STANDARDS
from retriever import retrieve_chunks

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")
client = OpenAI()

SYSTEM_PROMPT = """
You are a contract compliance reviewer.
You will receive a specific compliance clause and the most relevant sections retrieved from a contract.
Evaluate whether the clause is satisfied based only on the provided sections.

Return a single JSON object:
{
  "clause": "...",
  "status": "pass" | "fail" | "unclear",
  "confidence_score": 0-100,
  "explanation": "...",
  "evidence": "direct quote from the retrieved sections or null",
  "recommendation": "what to add or clarify, or null if pass",
  "assessed_risk": "high" | "medium" | "low" | "none"
}

Rules:
- Use "unclear" when the concept is mentioned but not sufficiently defined to be enforceable.
- Only use evidence found in the provided sections.
- Return ONLY the JSON object, no extra text.
"""

def validate_clause(clause: dict, retrieved_chunks: list[str]) -> dict:
    context = "\n\n---\n\n".join(retrieved_chunks)

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.1,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"CLAUSE TO CHECK:\n{clause['clause']}: {clause['description']}\n\nRETRIEVED CONTRACT SECTIONS:\n{context}"}
        ]
    )

    raw = response.choices[0].message.content.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw)

def validate_contract(collection, embeddings_model, standards=STANDARDS) -> list:
    results = []
    for clause in standards:
        chunks = retrieve_chunks(clause, collection, embeddings_model)
        result = validate_clause(clause, chunks)
        results.append(result)
    return results