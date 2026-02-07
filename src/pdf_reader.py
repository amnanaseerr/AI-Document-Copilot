import fitz  # PyMuPDF

def read_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)

    for page in doc:
        page_text = page.get_text("text")
        if page_text:
            text += page_text + " "

    doc.close()

    # remove extra spaces / glitches
    text = " ".join(text.split())
    return text
