from django.shortcuts import render, redirect
from user.models import User

def system(request):
    if request.session.get('logged'):
        user = User.objects.get(id=request.session["user_id"])
        return render(request, 'system.html', {"user": user})
    else:
        return redirect('/auth/login/')
    

def home(request):
    if request.session.get("logged"):
        user = User.objects.get(id=request.session["user_id"])
        return render(request, "home.html", {"user": user})
    return render(request, 'home.html')

