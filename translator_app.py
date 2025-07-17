import streamlit as st
import json

# Load dictionary from file
with open("terms_dict.json", "r", encoding="utf-8") as f:
    terms = json.load(f)

# Create reverse dictionary for Hebrew to English
reverse_terms = {v: k for k, v in terms.items()}

st.title("🚑 English ↔ Hebrew Medical Translator")

search_term = st.text_input("Enter a word in English or Hebrew:")

if search_term:
    search_term = search_term.strip().lower()

    # Try English to Hebrew
    result = terms.get(search_term.title())

    # If not found, try Hebrew to English
    if not result:
        result = reverse_terms.get(search_term)

    if result:
        st.success(f"✅ Translation: {result}")
    else:
        st.error("❌ Term not found in the dictionary.")
