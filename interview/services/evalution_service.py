def evaluate_answer(answer):
    score = 0

    strengths = []
    weaknesses = []
    suggestions = []

    answer_lower = answer.lower()
    words = answer.split()
    word_count = len(words)

    # 1. Length Analysis
    if word_count > 60:
        score += 3
        strengths.append("Answer is detailed.")
    else:
        weaknesses.append("Answer is too short.")
        suggestions.append("Try to explain your answer in more detail.")

    # 2. Keyword Analysis
    keywords = ["project", "experience", "skill", "team", "problem", "solution"]
    keyword_count = sum(1 for word in keywords if word in answer_lower)

    if keyword_count >= 3:
        score += 3
        strengths.append("Good use of relevant keywords.")
    else:
        weaknesses.append("Lacks relevant technical details.")
        suggestions.append("Include experience, skills, or projects.")

    # 3. Confidence Analysis
    confidence_words = ["i built", "i developed", "i implemented", "i solved"]
    if any(word in answer_lower for word in confidence_words):
        score += 2
        strengths.append("Shows confidence.")
    else:
        weaknesses.append("Lacks confidence in tone.")
        suggestions.append("Use confident language like 'I developed...'")

    # 4. Structure Analysis
    if "." in answer:
        score += 2
        strengths.append("Well structured answer.")
    else:
        weaknesses.append("Poor sentence structure.")
        suggestions.append("Break answer into clear sentences.")

    return {
        "score": score,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions": suggestions
    }