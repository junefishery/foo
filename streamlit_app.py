# Import streamlit library
import streamlit as st

# Import urllib library
import urllib

# Create a text input for the user to enter a list of words
words = st.text_input("Enter a list of words separated by commas", value="long,gift,master")

# Check if the user has entered any words
if words:
    # Split the words by commas and strip any whitespace
    words = [word.strip() for word in words.split(",")]

    # Create a Bing query in the desired format
    query = f"write a short story with these words involved: {', '.join(words)}"
    query_origin = query

    # Replace all spaces with "+" symbols
    # query = query.replace(" ", "+")

    # Encode the query for the URL
    query = urllib.parse.quote(query)

    # Create a Bing URL with the query
    url = f"https://www.bing.com/search?q={query}"

    # Display the query as a link
    st.write(f"**Your Bing query is:** {query_origin}")
    st.markdown(f'<a href="{url}" target="_blank"><button>Let Bing AI create a story</button></a>', unsafe_allow_html=True)
