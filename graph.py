
# ============================================================================
# FILE: graph.py (LangGraph Workflow Definition)
# ============================================================================
from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Any
from nodes import (
    extract_text_node,
    chunk_text_node,
    create_embeddings_node,
    analyze_document_node,
    summarize_document_node,
    qa_node
)

class GraphState(TypedDict):
    '''
    GraphState is the data that travels through the nodes channel of the graph
    Stores filepath, messages, vector_store, summary, context untill cleared
    '''
    file_path: str
    filename: str
    extracted_text: str
    chunks: List[str]
    analysis: dict
    vector_store: Any
    summary: str
    question: str
    answer: str
    context: List[str]

def should_continue_to_qa(state: GraphState) -> str:
    """Determine if we should route to QA or end"""
    if state.get("question"):
        return "qa"
    return "end"

def create_document_graph():
    """Create the LangGraph workflow for document processing"""
    workflow = StateGraph(GraphState)
    
    # Add nodes for document processing pipeline
    workflow.add_node("extract", extract_text_node)
    workflow.add_node("chunk", chunk_text_node)
    workflow.add_node("embed", create_embeddings_node)
    workflow.add_node("analyze", analyze_document_node)
    workflow.add_node("summarize", summarize_document_node)
    #workflow.add_node("qa", qa_node)
    
    # Define the processing flow
    workflow.set_entry_point("extract")
    workflow.add_edge("extract", "chunk")
    workflow.add_edge("chunk", "embed")
    workflow.add_edge("embed", "analyze")
    workflow.add_edge("analyze", "summarize")
    
    # Conditional routing: if question exists, go to QA, otherwise end
    #workflow.add_conditional_edges(
    #    "summarize",
    #    should_continue_to_qa,
    #    {
    #        "qa": "qa",
    #        "end": END
    #    }
    #)
    
    workflow.add_edge("summarize", END)
    
    return workflow.compile()

def create_qa_graph():
    """Create a minimal graph for QA only (reuses existing vector store)"""
    workflow = StateGraph(GraphState)
    
    # Only add QA node
    workflow.add_node("qa", qa_node)
    
    # Start directly at QA
    workflow.set_entry_point("qa")
    workflow.add_edge("qa", END)
    
    return workflow.compile()
