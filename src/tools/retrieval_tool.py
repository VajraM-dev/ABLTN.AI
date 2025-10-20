from langchain.tools import tool
from src.llm_config.vector_store_config import vector_store
from sentence_transformers import CrossEncoder
from src.tools.grader_tool import grader_tool

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def _reranker(retrieved_chunks, query):
    """A simple reranker that prioritizes documents containing more query terms."""

    pairs = [(query, chunk) for chunk in retrieved_chunks]

    scores = reranker.predict(pairs)

    reranked = sorted(zip(retrieved_chunks, scores), key=lambda x: x[1], reverse=True)

    return reranked

@tool #(response_format="content_and_artifact")
def retrieve_context(query: str):
    """
    Retrieve relevant context documents based on the input query.
    The documents are related to Ableton Live and its functionalities.

    Args:
        query (str): The input query string.
    Returns:
        List of reranked documents relevant to the query.
    
    """
    retrieved_docs = vector_store.similarity_search(query, k=4)

    reranked_docs = _reranker(
        [doc.page_content for doc in retrieved_docs], query
    )

    serialized = "\n\n".join(
        f"Source: {doc.metadata}\nContent: {content}"
        for content, score in reranked_docs
        for doc in retrieved_docs if doc.page_content == content
    )

    grades = grader_tool(query, [doc for doc in reranked_docs])

    return serialized, reranked_docs, grades