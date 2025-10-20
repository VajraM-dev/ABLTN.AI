from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

separators=[
    "\n\n",
    "\n",
    " ",
    ".",
    ",",
    "\u200b",  # Zero-width space
    "\uff0c",  # Full-width comma
    "\u3001",  # Ideographic comma
    "\uff0e",  # Full-width full stop
    "\u3002",  # Ideographic full stop
    "",
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=4000,
    chunk_overlap=800,
    separators=separators,
    add_start_index=True
)

def load_and_split_document(file_path: str):
    loader = PyMuPDFLoader(file_path)

    docs = loader.load()

    all_text = ""
    for doc in docs:
        all_text += doc.page_content + "\n\n"

    splits = text_splitter.split_text(all_text)

    print(f"Total chunks created: {len(splits)} from {len(docs)} document(s).")

    return splits