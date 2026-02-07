import re
from pdf_reader import read_pdf

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9., ]', '', text)
    return text.strip()


if __name__ == "__main__":
    pdf_path = "../data/sample.pdf"

    raw_text = read_pdf(pdf_path)
    cleaned_text = clean_text(raw_text)

    print("CLEANED TEXT (first 500 chars):\n")
    print(cleaned_text[:500])

    with open("../outputs/cleaned_text.txt", "w", encoding="utf-8") as f:
        f.write(cleaned_text)
