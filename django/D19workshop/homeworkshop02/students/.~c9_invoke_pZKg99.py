from django.shortcuts import render, redirect
from datetime import datetime 

# Create your views here.
def index(request):
    student = Student()
    
    return render(request, 'students/index.html')
    
def create(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    birthday = request.GET.get('birthday')
    age = request.GET.get('age')
    
    st
    return redirect("/students/")