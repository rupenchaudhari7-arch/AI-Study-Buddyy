def generate_quiz(summary):
    sentences = [s.strip() for s in summary.split(".") if s.strip()]
    quiz = []

    for i, sentence in enumerate(sentences[:5]):
        question = f"What is the main idea of: '{sentence[:60]}... ?'"
        quiz.append({
            "question": question,
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Option A"
        })

    return quiz
