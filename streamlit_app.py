import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_wikipedia():
    # Make a GET request to the Wikipedia home page
    res = requests.get('https://en.wikipedia.org/wiki/Special:Random')

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(res.text, 'html.parser')

    # Extract the title and content of the article
    title = soup.select('h1')[0].text
    content = soup.select('div.mw-parser-output')[0].text

    return title, content

title, content = scrape_wikipedia()

st.title("Random Wikipedia Article")
if st.button("Refresh"):
    title, content = scrape_wikipedia()

st.write("")
st.write("### Title:", title, "")
st.write("Content:", content)
