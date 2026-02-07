def find_relevant_chunks(chunks, question, top_k=3):
    question_words = set(question.lower().split())
    scored = []

    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(question_words & chunk_words)
        scored.append((score, chunk))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [chunk for score, chunk in scored[:top_k] if score > 0]
