import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt", quiet=True)

def clean_text(text):
    lines = text.split("\n")
    clean_lines = []

    for line in lines:
        line = line.strip().lower()
        if len(line) < 25:
            continue
        if line in clean_lines:
            continue
        clean_lines.append(line)

    return " ".join(clean_lines)


def generate_answer(pdf_text, question):
    pdf_text = clean_text(pdf_text)
    sentences = sent_tokenize(pdf_text)

    question_words = set(question.lower().split())
    scored = []

    for s in sentences:
        score = sum(1 for w in question_words if w in s)
        if score > 0:
            scored.append((score, s))

    scored = sorted(scored, reverse=True, key=lambda x: x[0])

    # 🔥 MAX 5 SHORT BULLET POINTS
    final_answers = []
    for _, sent in scored[:5]:
        sent = sent.capitalize()
        sent = sent.replace("  ", " ")
        final_answers.append(sent)

    if not final_answers:
        return ["PDF me is question ka clear answer nahi mila."]

    return final_answers
