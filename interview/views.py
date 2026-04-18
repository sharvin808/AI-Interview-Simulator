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
    
def submit_answer(request):
    if request.method == "POST":
        answer = request.POST.get("answer")

        result = evaluate_answer(answer)

        return render(request, "result.html", {
            "score": result["score"],
            "strengths": result["strengths"],
            "weaknesses": result["weaknesses"],
            "suggestions": result["suggestions"]
        })