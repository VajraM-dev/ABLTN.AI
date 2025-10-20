from langchain_postgres import PGVector
from src.embedding.embedding_model import embeddings
from dotenv import load_dotenv
import os
load_dotenv()

vector_store = PGVector(
    embeddings=embeddings,
    collection_name="ableton_manual_embeddings",
    connection=os.environ.get("PGVECTOR_URL")
)