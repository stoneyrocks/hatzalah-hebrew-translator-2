import streamlit as st
import json

# Load dictionary from file
with open("terms_dict.json", "r", encoding="utf-8") as f:
    terms = json.load(f)

st.title("Hatzalah Hebrew to English Terms Translator")

# Choose translation direction
direction = st.radio("Select translation direction:", ("English → Hebrew", "Hebrew → English"))

search_term = st.text_input("Enter a word or phrase:")

if search_term:
    search_term = search_term.strip().lower()
    matches = []

    if direction == "English → Hebrew":
        for eng, heb in terms.items():
            if search_term in eng.lower() or search_term in heb.lower():
                matches.append((eng, heb))
    else:  # Hebrew → English
        for eng, heb in terms.items():
            if search_term in heb.lower() or search_term in eng.lower():
                matches.append((eng, heb))

    if matches:
        st.success(f"✅ Matches found ({direction}):")
        for eng, heb in sorted(set(matches)):
            if direction == "English → Hebrew":
                st.write(f"**{eng}** ↔ **{heb}**")
            else:
                st.write(f"**{heb}** ↔ **{eng}**")
    else:
        st.warning("❌ No matches found.")
