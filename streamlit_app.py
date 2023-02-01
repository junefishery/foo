import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Medium article display")

url = st.text_input("Enter the URL of the Medium article:")

if url:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    paragraphs = soup.find_all("p", {"class": "pw-post-body-paragraph"})
    for p in paragraphs:
        st.write(p.get_text())
