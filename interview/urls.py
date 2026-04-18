from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('submit/',views.submit_answer, name='submit'),
    path('start/', views.start_interview, name='start'),
    
]