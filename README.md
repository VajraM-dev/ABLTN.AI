# Ableton Embeder

## Overview
The "Ableton Embeder" project is designed to process and manage embeddings for ableton 12 manual. It includes functionality for chunking documents, generating embeddings, and storing them in a vector database. This project is structured to handle PDF files and integrate with machine learning models for embedding generation.

## Project Structure

### Root Directory
- **main.py**: The entry point for the project.
- **pyproject.toml**: Configuration file for Python dependencies and project metadata.
- **uv.lock**: Lock file for managing dependencies.
- **README.md**: Project documentation (this file).

### `src/` Directory
Contains the main source code for the project.

#### `chunker/`
- **doc_chunker.py**: Handles loading and chunking using Docling.
- **langchain_loader.py**: Handles loading and chunking using Langchain.
- **pdf_splitter.py**: Splits PDF files into smaller sections.

#### `chunks/`
- **ableton_docs_chunks_enriched.jsonl**: Stores enriched document chunks in JSON Lines format. Use this if you want to directly want to use the chunks.

#### `embedding/`
- **embedding_model.py**: Defines the embedding model used for generating embeddings.
- **push_embeddings.py**: Pushes generated embeddings to a vector database.
- **vector_store_config.py**: Configuration for the vector store.

#### `files/`
- **live12-manual-en.pdf**: Example PDF file used for testing and processing.

## Getting Started

### Prerequisites
- Python 3.11 or higher
- Install dependencies using `uv sync`.

### Running the Project
1. Generate embeddings:
   ```bash
   uv run main.py
   ```