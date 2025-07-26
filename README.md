```markdown
# 🍽 AI Kitchen Assistant

Your smart AI-powered cooking companion that helps you:
- 👨‍🍳 Chat with an AI Chef
- 🍲 Find recipes based on ingredients you have
- 💡 Get cooking tips, substitutions, and techniques

Built with **Streamlit**, powered by **Spoonacular API** and **Tavily AI Chat API**.

---

## 🌟 Features

### ✅ AI Chef (Tavily)
Ask questions like:
- *"How do I boil an egg?"*
- *"What can I substitute for olive oil?"*
- *"How to cook pasta perfectly?"*

### ✅ Recipe Finder (Spoonacular)
Enter the ingredients you have — e.g., `egg, tomato` — and get:
- Matching recipes
- ✅ Used ingredients
- ❌ Missing ingredients
- 🔗 Recipe link

---

## 📸 Demo

![Demo Screenshot](screenshot.png)  
*(Add a real screenshot from your app if available)*

---

## 🚀 Tech Stack

| Tool            | Purpose                               |
|-----------------|----------------------------------------|
| Python          | Backend logic                          |
| Streamlit       | Frontend Web UI                        |
| Spoonacular API | Recipe suggestions                     |
| Tavily API      | AI-powered cooking chat                |

---

## 📁 Folder Structure

```

kitch/
├── app.py                  # Main Streamlit app
├── tavily\_utils.py         # Handles Tavily AI interaction
├── requirements.txt        # Dependencies
└── .streamlit/
└── secrets.toml        # API keys (not committed to GitHub)

````

---

## 🔑 Setup Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/ai-kitchen-assistant.git
cd ai-kitchen-assistant
````

### 2️⃣ Create `.streamlit/secrets.toml`

```toml
# .streamlit/secrets.toml
SPOONACULAR_API_KEY = "your_spoonacular_api_key"
TAVILY_API_KEY = "your_tavily_api_key"
```

> ⚠️ Do not commit this file to GitHub!

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 📦 Requirements

```text
streamlit
requests
```

---

## 🔐 API Keys

* Get your **Spoonacular API Key**: [https://spoonacular.com/food-api](https://spoonacular.com/food-api)
* Get your **Tavily API Key**: [https://app.tavily.com/](https://app.tavily.com/)

---

## ✨ Example Queries

* `"How to make a fluffy omelette?"`
* `"What can I cook with eggs, tomatoes, and cheese?"`
* `"What is the best way to bake a cake?"`

---

## 🙌 Author

**Thilak Bangera**
🔗 [LinkedIn](https://www.linkedin.com/in/thilak-bangera-b37629318)
💻 [GitHub](https://github.com/Thilakbangera)
