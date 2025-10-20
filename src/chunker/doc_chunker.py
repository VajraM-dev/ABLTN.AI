from pathlib import Path
from typing import List
from pydantic import BaseModel, Field, field_validator
from docling.chunking import HybridChunker
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
)

from docling.datamodel.base_models import InputFormat

class ChunkerConfig(BaseModel):
    model_id: str = Field(default="Qwen/Qwen3-Embedding-0.6B")
    embedding_dimensions: int = Field(default=1024, gt=0)
    max_tokens: int = Field(default=1024, gt=0)
    
    @field_validator('model_id')
    def validate_model_id(cls, v):
        if not v or not isinstance(v, str):
            raise ValueError("model_id must be non-empty string")
        return v

class DocumentSplitter:
    def __init__(self, config: ChunkerConfig):
        self.config = config
        try:
            self.chunker = HybridChunker(
                tokenizer=config.model_id, 
                max_tokens=config.max_tokens
            )
        except Exception as e:
            raise RuntimeError(f"Failed to initialize chunker: {e}")
    
    def _load_doc_split(self, file_path: Path) -> List[str]:
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        try:
            accelerator_options = AcceleratorOptions(
                num_threads=8, device=AcceleratorDevice.CUDA
            )

            pipeline_options = PdfPipelineOptions()
            pipeline_options.accelerator_options = accelerator_options

            converter = DocumentConverter(format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=pipeline_options,
                )
            })
            
            doc = converter.convert(file_path).document
            chunk_iter = self.chunker.chunk(dl_doc=doc)

            enriched_text = []
            for _, chunk in enumerate(chunk_iter):
                enriched_text.append(self.chunker.contextualize(chunk=chunk) + "\n\n")

            return enriched_text
        except Exception as e:
            raise RuntimeError(f"Failed to load document: {e}")

    def _club_chunks(self, chunks: List[str], max_tokens: int) -> List[str]:
        if not chunks:
            return []
        
        result = []
        current_batch = []
        current_tokens = 0
        
        for chunk in chunks:
            if not chunk or not chunk.strip():
                continue
                
            chunk_tokens = len(chunk.split())
            
            if current_tokens + chunk_tokens <= max_tokens:
                current_batch.append(chunk)
                current_tokens += chunk_tokens
            else:
                if current_batch:
                    result.append(' '.join(current_batch))
                current_batch = [chunk]
                current_tokens = chunk_tokens
        
        if current_batch:
            result.append(' '.join(current_batch))
        
        return result
    
    def load_and_club(self, file_path: str) -> List[str]:
        print(f"Loading and chunking document: {file_path}")
        try:

            splits = self._load_doc_split(file_path)

            if not splits:
                return "Error creating chunks from chunker. Got empty list."
            
            splits = self._club_chunks(splits, self.config.max_tokens)
            
            return splits
            
        except Exception as e:
            return f"Error creating chunks: {e}"