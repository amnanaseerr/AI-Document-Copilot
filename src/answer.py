def generate_answer(relevant_chunks, question):
    if not relevant_chunks:
        return "PDF me is question ka relevant answer nahi mila."

    answer = "📌 Answer from PDF:\n\n"

    for i, chunk in enumerate(relevant_chunks, 1):
        answer += f"{i}. {chunk.strip()[:400]}...\n\n"

    return answer
