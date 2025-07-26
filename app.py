import streamlit as st
import requests
from tavily_utils import chat_with_tavily  # helper file for Tavily API

st.set_page_config(page_title="🍽 AI Kitchen Assistant")
st.title("🍽 AI Kitchen Assistant")
st.caption("Your smart companion for recipes and cooking tips!")

# ----------- Spoonacular Recipe Fetcher ------------
def get_recipes(ingredients):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ingredients,
        "number": 3,
        "apiKey": st.secrets["SPOONACULAR_API_KEY"]
    }
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        st.error(f"Failed to fetch recipes: {e}")
        return []

# ----------- Initialize Session State ------------
for key in ["chat_input", "chat_response", "recipe_input", "recipe_data"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# ----------- AI Chat Section ------------
st.subheader("🤖 Chat with Your AI Chef")

st.session_state.chat_input = st.text_area(
    "Ask me anything — cooking tips, ingredient swaps, techniques, and more!",
    value=st.session_state.chat_input,
    key="chat_input_area"
)

if st.button("Ask AI"):
    if st.session_state.chat_input.strip():
        with st.spinner("Thinking..."):
            st.session_state.chat_response = chat_with_tavily(st.session_state.chat_input)
    else:
        st.warning("Please enter a question.")

if st.session_state.chat_response:
    st.markdown(f"👨‍🍳 **AI Chef says:**\n\n{st.session_state.chat_response}")

# ----------- Recipe Finder Section ------------
st.subheader("🍲 Recipe Finder")
recipe_input = st.text_input("What ingredients do you have?", placeholder="e.g., egg, tomato")

if st.button("Find Recipes"):
    if recipe_input.strip():
        with st.spinner("Fetching recipes..."):
            recipes = get_recipes(recipe_input.strip())
            if recipes:
                st.session_state.recipe_input = recipe_input.strip()
                st.session_state.recipe_data = recipes
            else:
                st.warning("No recipes found.")
    else:
        st.warning("Please enter at least one ingredient.")

# ----------- Show Previous Recipe Results (Persisted) ------------
if st.session_state.recipe_data:
    st.markdown(f"### 🍳 Recipes using: `{st.session_state.recipe_input}`")
    for recipe in st.session_state.recipe_data:
        st.image(recipe["image"], width=250)
        recipe_link = f"https://spoonacular.com/recipes/{recipe['title'].lower().replace(' ', '-')}-{recipe['id']}"
        st.markdown(f"### [{recipe['title']}]({recipe_link})")
        st.markdown(f"✅ Used: {', '.join([i['name'] for i in recipe['usedIngredients']])}")
        st.markdown(f"❌ Missing: {', '.join([i['name'] for i in recipe['missedIngredients']])}")
        st.markdown("---")
