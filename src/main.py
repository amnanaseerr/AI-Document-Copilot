import os
from utils.pdf_reader import extract_text_from_pdf
from utils.chunker import chunk_text
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Files
pdf_file = "sample.pdf"
index_file = "index_file.pkl"
chunks_file = "chunks_file.pkl"

# Step 1: Extract PDF text
text = extract_text_from_pdf(pdf_file)

# Step 2: Chunk text
chunks = chunk_text(text)

# Step 3: Initialize model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 4: Build or load vector store
if os.path.exists(index_file) and os.path.exists(chunks_file):
    with open(index_file, 'rb') as f:
        index = pickle.load(f)
    with open(chunks_file, 'rb') as f:
        chunks = pickle.load(f)
else:
    vectors = model.encode(chunks)
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    # Save for future use
    with open(index_file, 'wb') as f:
        pickle.dump(index, f)
    with open(chunks_file, 'wb') as f:
        pickle.dump(chunks, f)

print("📄 PDF Copilot Ready!")
print("Type your question (or 'exit' to quit)")

# Interactive loop
while True:
    query = input("\n❓ Ask: ")
    if query.lower() == "exit":
        print("👋 Goodbye!")
        break

    query_vec = model.encode([query])
    D, I = index.search(query_vec, k=3)  # Top 3 relevant chunks
    if len(I[0]) == 0:
        print("❌ No relevant answer found.")
        continue

    print("\n📌 Relevant content:\n")
    for idx in I[0]:
        print("-", chunks[idx])
