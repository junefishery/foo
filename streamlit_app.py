import wikipediaapi
import streamlit as st

wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

st.title("Random Wikipedia Article")

if st.button("Get Random Article"):
    random_title = wiki_wiki.random()
    page = wiki_wiki.page(random_title)
    st.write("Title: ", page.title)
    st.write("Summary: ", page.summary[0:500] + "...")
