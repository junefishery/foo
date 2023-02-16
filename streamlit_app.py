import streamlit as st
import urllib
import re
import pandas as pd
import random

# Set the page config
st.set_page_config(
    layout="centered", # or "centered"
    initial_sidebar_state="auto", # or "expanded" or "collapsed"
    page_title="WordGPT", # or any other title
    page_icon="📝" # or any other emoji or image
)

# Give a large title to the page
st.title("WordGPT")

# read the csv file
df = pd.read_csv("ielts.csv")

# create two columns
col1, col2 = st.columns(2)

# get all the values from the first column of the dataframe as a list
values = df.iloc[:,0].tolist()

# join the values with newline characters as a string
text = "\n".join(values)

placeholder = col1.empty()

# display the value in the textarea of the first column
words = placeholder.text_area("Value from ielts.csv", text, height=200)

# Create a button in col1 named "Shuffle the words"
shuffle_button = col1.button("Shuffle the words")

# Shuffle the words in the text area and display them in col2
if shuffle_button:
    words = words.split("\n")
    random.shuffle(words)
    words = "\n".join(words)
    placeholder.empty()
    words = placeholder.text_area("Shuffle the words", words, height=200)

# Check if the user has entered any words
if words:
    # Split the words by any common symbol or line break and strip any whitespace
    words = [word.strip() for word in re.split("[,.;:!?]|\\n", words)]

    # Select only the first 12 words of the list
    words = " ".join(re.findall(r"\w+", " ".join(words))[:12])

    # Create a Bing query in the desired format
    query = f"write a short story with these words involved: {words}"
    query_origin = query

    # Replace all spaces with "+" symbols
    # query = query.replace(" ", "+")

    # Encode the query for the URL
    query = urllib.parse.quote(query)

    # Create a Bing URL with the query
    url = f"https://www.bing.com/search?q={query}"

    # Put the rest of the elements in the right column
    col2.write(f"**Your Bing query is:** {query_origin}")
    col2.markdown(f'<a href="{url}" target="_blank"><button>Let Bing AI create a story</button></a>', unsafe_allow_html=True)

    # Create a form in the right column with the clear_on_submit parameter set to True
    with col2.form("story_form", clear_on_submit=True):
        # Put a textarea in the form
        story = st.text_area("Enter your own story or edit the Bing AI story", value="", height=200)

        # Put a submit button in the form
        submitted = st.form_submit_button("Submit")

        # Check if the user has submitted the form
        if submitted:
            # Open the file in append mode
            with open("my_story.txt", "a") as f:
                # Write the story to the file
                f.write(story + "\n")
