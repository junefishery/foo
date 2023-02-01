import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Medium article display")

url = st.text_input("Enter the URL of the Medium article:")

if url:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    paragraphs = soup.find_all("p", {"class": "pw-post-body-paragraph"})
    article_content = "\n\n".join([p.get_text() for p in paragraphs])
    text_area = st.text_area(article_content, key='text_area')
    if st.button("Select text"):
        st.write("""
        <script>
            document.getElementById("text_area-0").select();
        </script>
        """, unsafe_allow_html=True)
