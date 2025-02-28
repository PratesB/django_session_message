from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from hashlib import sha256

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        errors = []

        if not name or not name.strip():
            errors.append("Name cannot be empty")

        if not email or not email.strip():
            errors.append("Email cannot be empty")

        if len(password) < 5:
            errors.append("Your password must be at least 5 characters long")
        
        if User.objects.filter(email=email).exists():
            errors.append("There is already a user with that email.")

        
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect("register")
        

        password_hash = sha256(password.encode()).hexdigest()

        try:
            User.objects.create(name=name, email=email, password=password_hash)
            messages.success(request, "Your account has been successfully created. Log in now to begin using the system.")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Internal error: {e}")
            return redirect("register")

    return render(request, "register.html")



def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_hash = sha256(password.encode()).hexdigest()

        try:
            user = User.objects.get(email=email, password=password_hash)
            request.session["logged"] = True
            request.session["user_id"] = user.id
            return redirect("system")
        except User.DoesNotExist:
            messages.warning(request, "Invalid email or password.")
            return redirect("login")
    return render(request, "login.html")



def logout(request):
    request.session.flush()
    messages.success(request, "Logout successful!")
    return redirect("login")



def delete_account(request):
    if not request.session.get("logged"):
        messages.error(request, "You must be logged in to delete your account.")
        return redirect("login")
    
    user = User.objects.get(id=request.session["user_id"])
    
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_hash = sha256(password.encode()).hexdigest()


        try:
            user = User.objects.get(email=email, password=password_hash)
            user.delete()
            request.session.flush()
            messages.success(request, "Your account has been permanently deleted.")
            return redirect("login")
        
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password. Account deletion failed.")
            return redirect("delete_account")
        
        except Exception as e:
            messages.error(request, f"Internal error: {e}")
            return redirect("delete_account")
    
    return render(request, "delete_account.html", {"user": user})



def edit_account(request):
    if not request.session.get("logged"):
        messages.error(request, "You must be logged in to edit your account")
        return redirect("login")

    user = User.objects.get(id=request.session["user_id"])

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        new_password = request.POST.get("new_password")

        if name:
            user.name = name
        if email:
            user.email = email

        if password and new_password:
            password_hash = sha256(password.encode()).hexdigest()
            if password_hash == user.password:
                new_password_hash = sha256(new_password.encode()).hexdigest()
                user.password = new_password_hash
            else:
                messages.error(request, "Incorret current password")
                return redirect("edit_account")
        else:
            messages.error(request, "Please, enter your password and your new password")
            return redirect("edit_account")

        user.save()
        messages.success(request, "Your account has been updated")
        return redirect("edit_account")

    return render(request, "edit_account.html", {"user": user})

        




    