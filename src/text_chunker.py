from text_cleaner import clean_text
from pdf_reader import read_pdf

def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


if __name__ == "__main__":
    pdf_path = "../data/sample.pdf"

    raw_text = read_pdf(pdf_path)
    cleaned_text = clean_text(raw_text)

    chunks = chunk_text(cleaned_text)

    print(f"TOTAL CHUNKS CREATED: {len(chunks)}\n")
    print("SAMPLE CHUNK:\n")
    print(chunks[0])

    with open("../outputs/text_chunks.txt", "w", encoding="utf-8") as f:
        for i, chunk in enumerate(chunks):
            f.write(f"--- CHUNK {i+1} ---\n")
            f.write(chunk + "\n\n")
