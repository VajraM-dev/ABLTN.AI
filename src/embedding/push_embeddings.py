from src.embedding.vector_store_config import vector_store
from langchain_core.documents import Document
import tiktoken
import uuid

def create_unique_id(number_of_ids: int):
    return [str(uuid.uuid4()) for _ in range(number_of_ids)]

# def push_embeddings(docs_with_embeddings):

def push_embeddings(docs_with_embeddings, model_name="text-embedding-3-large", safety_factor=0.9):
    # Prepare docs and metadata
    docs = [Document(page_content=doc, metadata={"source": "https://cdn-resources.ableton.com/resources/pdfs/live-manual/12/2025-10-16/live12-manual-en.pdf"}) 
            for doc in docs_with_embeddings]

    # Token estimator setup
    enc = tiktoken.encoding_for_model(model_name)

    # Batch docs
    batch = []
    batch_tokens = 0
    max_tokens = 300_000 * safety_factor  # e.g., 270k to be safe

    for doc in docs:
        num_tokens = len(enc.encode(doc.page_content))
        # If adding this doc would exceed batch limit, flush current batch
        if batch and (batch_tokens + num_tokens) > max_tokens:
            vector_store.add_documents(documents=batch)
            print(f"Pushed batch of {len(batch)} docs (~{batch_tokens} tokens)")
            batch = []
            batch_tokens = 0

        batch.append(doc)
        batch_tokens += num_tokens

    # Push final batch
    if batch:
        vector_store.add_documents(documents=batch)
        print(f"Pushed final batch of {len(batch)} docs (~{batch_tokens} tokens)")

    print(f"Total pushed {len(docs)} documents.")
    return True