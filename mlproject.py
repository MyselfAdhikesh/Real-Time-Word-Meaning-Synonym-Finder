import streamlit as st
import nltk
from nltk.corpus import wordnet
from textblob import Word

# Download necessary NLTK data (only needed once)
nltk.download('wordnet')
nltk.download('omw-1.4')

# Function to get the word meaning
def get_word_meaning(word):
    synonyms = wordnet.synsets(word)
    if synonyms:
        return synonyms[0].definition()
    else:
        return "No definition found."

# Function to get related (synonym) words
def get_related_words(word):
    blob = Word(word)
    try:
        return blob.synsets  # Using synsets as .synonym() is not a real method
    except:
        return []

# Streamlit app layout
st.title("📚 Real-Time Word Meaning & Synonym Finder")

word_input = st.text_input("Enter a word:")

if word_input:
    meaning = get_word_meaning(word_input)
    related = get_related_words(word_input)

    st.subheader("Meaning:")
    st.write(meaning)

    st.subheader("Related Words (Synonyms):")
    if related:
        synonyms = set()
        for syn in related:
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
        st.write(", ".join(synonyms) if synonyms else "No synonyms found.")
    else:
        st.write("No synonyms found.")
