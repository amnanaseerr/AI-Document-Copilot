import re
from nltk.tokenize import sent_tokenize

def clean_and_format_answer(text, max_points=5):
    sentences = sent_tokenize(text)

    bullets = []
    for s in sentences:
        s = re.sub(r'\s+', ' ', s).strip()
        if len(s) > 25 and len(s) < 220:
            bullets.append(s)
        if len(bullets) == max_points:
            break

    # force bullet on NEW LINE
    formatted = ""
    for b in bullets:
        formatted += f"• {b}\n\n"

    return formatted.strip()
