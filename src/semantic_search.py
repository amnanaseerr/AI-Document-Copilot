import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

def load_embeddings(path="../outputs/embeddings.pkl"):
    with open(path, "rb") as f:
        chunks, embeddings = pickle.load(f)
    return chunks, embeddings


def semantic_search(query, chunks, embeddings, model, top_k=1):
    query_embedding = model.encode([query])[0]

    similarities = np.dot(embeddings, query_embedding) / (
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_embedding)
    )

    top_indices = similarities.argsort()[-top_k:][::-1]
    return [(chunks[i], similarities[i]) for i in top_indices]


if __name__ == "__main__":
    chunks, embeddings = load_embeddings()
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("\n📄 AI DOC COPILOT")
    print("Type your question below.")
    print("Type 'exit' or 'quit' to close.\n")

    while True:
        query = input(">> ").strip()

        if query.lower() in ["exit", "quit"]:
            print("\n👋 Exiting AI Doc Copilot. Goodbye!")
            break

        if query == "":
            print("⚠️ Please enter a question.\n")
            continue

        results = semantic_search(query, chunks, embeddings, model)

        print("\n🤖 MOST RELEVANT ANSWER:\n")
        print(results[0][0])
        print("\n" + "-"*60 + "\n")
