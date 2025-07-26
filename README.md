# 🍽 AI Kitchen Assistant

A text-enabled cooking companion powered by *FastAPI, **Streamlit, **Whisper, and **LLaMA 3. This assistant helps you **generate recipes, **chat with an AI chef, and even **transcribe voice commands* to offer personalized cooking suggestions.

---

## 🚀 Features

- 🧾 *Ingredient-Based Recipe Search* via Spoonacular API
- 🤖 *Chat with an AI Chef* powered by Ollama (LLaMA 3 model)
- ⚡ FastAPI backend with fully interactive Streamlit frontend
- 🔐 Secrets management using st.secrets for API key security

---

## 🧠 Tech Stack

| Layer        | Technology                        |
|--------------|-----------------------------------|
| 🧠 AI Models | Whisper (speech → text), Ollama LLaMA3 (chat) |
| 🧪 Backend    | FastAPI, Uvicorn                  |
| 🎛 Frontend  | Streamlit                         |
| 📡 API       | Spoonacular API (for recipes)     |

---

## 📁 Folder Structure
ai-kitchen-assistant/
├── app.py                  # FastAPI backend server
├── frontend.py             # Streamlit frontend interface
├── requirements.txt        # Project dependencies
├── secrets.toml            # Spoonacular API key config
