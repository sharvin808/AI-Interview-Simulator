from django.shortcuts import render
from .services.ai_service import generate_question
from .services.evalution_service import evaluate_answer

def home(request):
    if request.method == "POST":
        role = request.POST.get('role')

        question = generate_question(role)

        return render(request,'interview.html',{
            'question':question,                        
            'role':role
            })
    return render(request,'home.html')

def start_interview(request):
    if request.method == "POST":
        role = request.POST.get("role")

        request.session["role"] = role
        request.session["current_q"] = 1
        request.session["scores"] = []

        question = generate_question(role)

        return render(request, "interview.html", {
            "question": question,
            "q_no": 1
        })

TOTAL_QUESTIONS = 3

def submit_answer(request):
    if request.method == "POST":
        answer = request.POST.get("answer")

        result = evaluate_answer(answer)

        # Save score
        scores = request.session.get("scores", [])
        scores.append(result["score"])
        request.session["scores"] = scores

        current_q = request.session.get("current_q", 1)

        # Next question
        if current_q < TOTAL_QUESTIONS:
            request.session["current_q"] = current_q + 1

            role = request.session.get("role")
            question = generate_question(role)

            return render(request, "interview.html", {
                "question": question,
                "q_no": current_q + 1
            })

        # Final result
        total_score = sum(scores)
        avg_score = total_score / TOTAL_QUESTIONS

        return render(request, "final_result.html", {
            "total_score": total_score,
            "avg_score": round(avg_score, 2)
        })