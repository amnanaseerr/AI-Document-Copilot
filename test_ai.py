from src.pdf_reader import read_pdf
import re

def find_answer(pdf_text, question):
    pdf_text = pdf_text.lower()
    lines = [l.strip() for l in pdf_text.split("\n") if len(l.strip()) > 20]

    keywords = ["ai", "artificial", "intelligence"]
    bad_starters = ("introduction", "contents", "table", "section", "chapter")

    scored = []

    for i, line in enumerate(lines):
        if line.startswith(bad_starters):
            continue

        words = re.findall(r"\b\w+\b", line)
        score = 0

        for kw in keywords:
            if kw in words:
                score += 2

        if " is " in line or " means " in line or " defined as " in line:
            score += 3

        if score > 0:
            context = line

            # attach next line if it continues the thought
            if i + 1 < len(lines):
                if not lines[i + 1].startswith(bad_starters):
                    context += " " + lines[i + 1]

            scored.append((score, context))

    if not scored:
        return "❌ Is question ka answer PDF me nahi mila."

    scored.sort(reverse=True)
    answer = scored[0][1]

    # formatting
    answer = answer.capitalize()
    if not answer.endswith("."):
        answer += "."

    return "📘 PDF se relevant answer:\n\n" + answer


pdf_path = input("PDF path: ")
question = input("Your question: ")

pdf_text = read_pdf(pdf_path)
answer = find_answer(pdf_text, question)

print("\n" + answer)
