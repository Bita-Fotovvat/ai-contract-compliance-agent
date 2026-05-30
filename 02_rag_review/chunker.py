"""
chunker.py
----------
This file is responsible for splitting the extracted contract text into smaller pieces
called "chunks". This is a critical step in any RAG pipeline.

Large language models have a context window limit, they can only read so much text
at once. More importantly, sending an entire 10-page contract to find one clause is
inefficient and noisy. By splitting the contract into small overlapping segments,
we can later retrieve only the chunks that are relevant to each specific clause.

chunk_size=500 means each chunk is approximately 500 characters long.
chunk_overlap=100 means consecutive chunks share 100 characters, so a clause that
sits near a boundary does not get cut in half and missed entirely.

Library used: langchain (RecursiveCharacterTextSplitter)
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text: str) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " "]
    )
    return splitter.split_text(text)