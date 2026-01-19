
# ============================================================================
# FILE: utils/text_chunker.py
# ============================================================================
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = chunk_size,
    chunk_overlap = overlap,
    length_function = len,
    separators=["\n\n", "\n", ". ", " ", ""]
    )

    chunks = text_splitter.split_text(text)

    return chunks

