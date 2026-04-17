from django.shortcuts import render
from .services.ai_service import generate_question

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
        answer = request.POST.get('answer')

        feedback = "Good attempt! Try to be more detailed."

        return render(request,'result.html',{
            'answer':answer,
            'feedback':feedback
        })
