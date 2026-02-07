from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_vector_store(chunks):
    embeddings = model.encode(chunks)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return index, chunks


def search_answer(question, index, chunks, k=3):
    q_embedding = model.encode([question])
    distances, indices = index.search(np.array(q_embedding), k)

    results = []
    for idx in indices[0]:
        results.append(chunks[idx])

    return " ".join(results)
