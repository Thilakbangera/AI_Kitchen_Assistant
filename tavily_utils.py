import requests
import streamlit as st

def chat_with_tavily(message: str) -> str:
    """
    Uses Tavily's /search endpoint to answer a user query.
    Requires TAVILY_API_KEY in Streamlit secrets.
    """
    url = "https://api.tavily.com/search"
    headers = {
        "Authorization": f"Bearer {st.secrets['TAVILY_API_KEY']}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": message,
        "include_answer": True
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json().get("answer", "No answer found.")
    except Exception as e:
        return f"❌ Error from Tavily: {e}"
