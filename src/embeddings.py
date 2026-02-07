from sentence_transformers import SentenceTransformer
from text_chunker import chunk_text
from text_cleaner import clean_text
from pdf_reader import read_pdf
import pickle

def create_embeddings(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)
    return embeddings


if __name__ == "__main__":
    pdf_path = "../data/sample.pdf"

    raw_text = read_pdf(pdf_path)
    cleaned_text = clean_text(raw_text)
    chunks = chunk_text(cleaned_text)

    embeddings = create_embeddings(chunks)

    print("Embeddings created!")
    print("Shape:", embeddings.shape)

    with open("../outputs/embeddings.pkl", "wb") as f:
        pickle.dump((chunks, embeddings), f)
