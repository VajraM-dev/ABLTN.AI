import os
import orjson
from src.chunker.langchain_loader import load_and_split_document
from src.embedding.push_embeddings import push_embeddings

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "src", "files", "live12-manual-en.pdf")

def create_splits(file_path: str):
    chunks = load_and_split_document(file_path=file_path)

    if os.path.exists(os.path.join(dir_path, "src", "chunks", "ableton_docs_chunks_enriched.jsonl")):
        print("Chunks file already exists, skipping creation.")
        return chunks

    with open(os.path.join(dir_path, "src", "chunks", "ableton_docs_chunks_enriched.jsonl"), "wb") as f:
        for chunk in chunks:
            f.write(orjson.dumps({"text": chunk}) + b"\n")

    return chunks

if __name__ == "__main__":
    print(file_path)

    chunks = create_splits(file_path=file_path)
    push_embeddings(chunks)


    