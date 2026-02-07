import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk

# ensure required data
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

stop_words = set(stopwords.words("english"))

def clean_words(text):
    words = word_tokenize(text.lower())
    return [
        w for w in words
        if w.isalnum() and w not in stop_words
    ]

def find_answer(pdf_text, question):
    if not pdf_text.strip():
        return "PDF empty hai."

    sentences = sent_tokenize(pdf_text)
    question_words = set(clean_words(question))

    scored = []

    for sent in sentences:
        sent_words = set(clean_words(sent))
        score = len(question_words & sent_words)
        if score > 0:
            scored.append((score, sent))

    if not scored:
        return "PDF me is question ka clear answer nahi mila."

    # best matches
    scored.sort(reverse=True, key=lambda x: x[0])
    top_sentences = [s[1] for s in scored[:2]]

    return " ".join(top_sentences)
