from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def mypage(request):
    return render(request, "mypage.html")

def incollege(request):
    return render(request, "incollege.html")

def myproject(request):
    return render(request, "myproject.html")

def contact(request):
    return render(request, "contact.html")

def INPROJECT(request):
    return render(request, "INPROJECT.html")

def _grade(request):
    return render(request, "1&2.html")