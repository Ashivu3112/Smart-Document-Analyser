# ============================================================================
# FILE: utils/llm_client.py
# ============================================================================
from openai import OpenAI
import os

def get_chatgpt_response(prompt: str, max_tokens: int = 2000) -> str:
    """Get response from openai API"""
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", ""))
    
    response = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=max_tokens,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content