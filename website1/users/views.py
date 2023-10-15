from django.shortcuts import render

def log(request):
    return render(request,'login.html')

def sign(request):
    
    return render(request,'signup.html')