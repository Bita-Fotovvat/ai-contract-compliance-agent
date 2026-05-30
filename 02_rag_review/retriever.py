"""
retriever.py
------------
This file is responsible for querying ChromaDB to find the most relevant contract
chunks for each compliance clause.

This is the "R" in RAG — the Retrieval step.

How it works:
For each clause in our standards (e.g. "Payment Schedule"), we build a search query
from the clause name and description. That query is embedded into a vector using the
same embedding model used in embedder.py. ChromaDB then compares that query vector
against all stored chunk vectors and returns the n_results chunks whose meaning is
most similar to the query.

For example, searching for:
    "Payment Schedule: define deposit, progress payments, and due dates"
will retrieve contract chunks that talk about deposits, payment milestones, or
amounts due — even if they use different wording than the query.

This means GPT only receives the 3 most relevant chunks per clause instead of the
entire contract, making the analysis more focused and accurate.

Libraries used: chromadb (via embedder.py collection object)
"""

def retrieve_chunks(clause: dict, collection, embeddings_model, n_results: int = 3) -> list[str]:
    query = f"{clause['clause']}: {clause['description']}"
    query_embedding = embeddings_model.embed_query(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]