# ============================================================================
# FILE: utils/prompts.py
# ============================================================================

ANALYSIS_PROMPT = """Analyze the following document excerpt and provide:
1. Main topics/themes
2. Key entities (people, organizations, places)
3. Document type and structure

Document excerpt:
{text}

Provide a structured analysis in JSON format."""

SUMMARY_PROMPT = """Generate a comprehensive summary of the following document.
Include:
- Main purpose and key points
- Important findings or conclusions
- Significant details

Document:
{text}

Provide a clear, concise summary."""

QA_PROMPT = """You are a helpful assistant answering questions about a document.
Use ONLY the information from the provided context to answer the question.
If the answer cannot be found in the context, say so clearly.

Context:
{context}

Question: {question}

Answer the question based solely on the context provided above."""