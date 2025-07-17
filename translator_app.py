import streamlit as st
import json

# Load dictionary from file
with open("terms_dict.json", "r", encoding="utf-8") as f:
    terms = json.load(f)

# Create reverse dictionary for Hebrew to English
reverse_terms = {v: k for k, v in terms.items()}

st.title("Hatzalah Hebrew to English Terms Translator")

search_term = st.text_input("Enter a word in English or Hebrew:")

if search_term:
    search_term = search_term.strip().lower()

    # Match any phrase containing the search term
    matches = []
    for eng, heb in terms.items():
        if search_term in eng.lower() or search_term in heb.lower():
            matches.append((eng, heb))

    for heb, eng in reverse_terms.items():
        if search_term in heb.lower() or search_term in eng.lower():
            matches.append((eng, heb))

    # Remove duplicates
    matches = list(set(matches))

    if matches:
        st.success("✅ Matches found:")
        for eng, heb in sorted(matches):
            st.write(f"**{eng}** ↔ **{heb}**")
    else:
        st.warning("❌ No matches found.")
