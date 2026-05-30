"""
embedder.py
-----------
This file is responsible for converting text chunks into embeddings and storing
them in ChromaDB, a vector database.

An embedding is a list of numbers (a vector) that represents the meaning of a
piece of text. Text with similar meaning produces similar vectors. This is what
allows semantic search to work; instead of matching keywords, we match meaning.

What happens here step by step:
1. We take all the chunks produced by chunker.py
2. We send each chunk to OpenAI's embedding model (text-embedding-3-small)
3. OpenAI returns a vector for each chunk
4. We store both the original text and its vector in ChromaDB
5. ChromaDB can now be queried: "find me the chunks most similar to this query"

The collection is recreated fresh on every run so that a new contract upload
does not mix with a previous one.

Libraries used: chromadb, langchain-openai
"""

import chromadb
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

def build_vector_store(chunks: list[str], collection_name: str = "contract"):
    client = chromadb.Client()

    try:
        client.delete_collection(collection_name)
    except:
        pass

    collection = client.create_collection(collection_name)
    embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")
    embeddings = embeddings_model.embed_documents(chunks)

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )

    return collection, embeddings_model