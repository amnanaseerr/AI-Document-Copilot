import streamlit as st
import tempfile
from src.pdf_reader import read_pdf
from src.text_utils import clean_and_format_answer

st.set_page_config(
    page_title="AI PDF Copilot",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #2b143f;
}
h1, h2, h3, p, label {
    color: #f3e8ff !important;
}
div[data-testid="stFileUploader"],
div[data-testid="stTextInput"] {
    background-color: #3d1b5a;
    border-radius: 14px;
    padding: 12px;
}
.stButton>button {
    background-color: #7a3cff;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'> AI PDF Copilot</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "📄 Upload any PDF",
    type=["pdf"]
)

if uploaded_file:
    question = st.text_input("❓ Ask a question from this PDF")

    if question:
        with st.spinner("🧠 Reading PDF & generating smart answer..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                pdf_path = tmp.name

            pdf_text = read_pdf(pdf_path)

            # simple semantic extraction (offline, fast)
            final_answer = clean_and_format_answer(pdf_text)

        st.markdown("### 📘 Answer")
        st.markdown(final_answer)
