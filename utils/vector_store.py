
# ============================================================================
# FILE: utils/vector_store.py
# ============================================================================
import chromadb
from chromadb.config import Settings
from typing import List
import hashlib

def create_vector_store(chunks: List[str]) -> chromadb.Collection:
    """Create ChromaDB vector store from text chunks"""
    # Initialize ChromaDB client
    client = chromadb.Client(Settings(
        anonymized_telemetry=False,
        is_persistent=False
    ))
    
    # Create or get collection
    collection_name = "document_collection"
    
    # Delete existing collection if it exists
    try:
        client.delete_collection(collection_name)
    except:
        pass
    
    collection = client.create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"}
    )
    
    # Add documents to collection
    ids = [hashlib.md5(chunk.encode()).hexdigest() for chunk in chunks]
    
    collection.add(
        documents=chunks,
        ids=ids
    )
    
    return collection

def retrieve_relevant_chunks(
    vector_store: chromadb.Collection,
    query: str,
    top_k: int = 3
) -> List[str]:
    """Retrieve most relevant chunks for a query using RAG"""
    results = vector_store.query(
        query_texts=[query],
        n_results=top_k
    )
    
    # Extract documents from results
    if results and 'documents' in results and results['documents']:
        return results['documents'][0]
    
    return []

