import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Medium article display")

url = st.text_input("Enter the URL of the Medium article:")

if url:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    paragraphs = soup.find_all("p", {"class": "pw-post-body-paragraph"})
    article_content = "\n".join([p.get_text() for p in paragraphs])

    # Display the article content
    text_area = st.text_area("Article content", article_content, key="content")
    
    # Add a select all button
    if st.button("Select all"):
        text_area.text.set(article_content)
