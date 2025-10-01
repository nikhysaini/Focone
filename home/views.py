from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import random
from accounts.models import Customuser

User = Customuser
def focusmode(request):
    return render(request,"focus.html")

def index(request):
    return render(request,"focone.html")

def profile(request):
    return render(request,"profile.html")

def editprofile(request):
    if request.method == "POST":
      user = User.objects.get(pk=request.user.id)
      user.first_name=request.POST.get('firstname')
      user.last_name=request.POST.get('lastname')
      user.email = request.POST.get('email')
      user.bio = request.POST.get('bio')
      user.profession = request.POST.get('profession')
      user.country = request.POST.get('country')
      user.save()
      return render(request, "profile_page.html")
    return render(request, "profile_page.html")

def register_view(request):
    if request.method != "POST":
        return render(request, "focone.html")
    
    if not request.POST.get("otp"):
        session_data = {
            'firstname': request.POST.get("firstname"),
            'lastname': request.POST.get("lastname"),
            'email': request.POST.get("email"),
            'password': request.POST.get("password"),
            'profile_picture': request.FILES.get("profile").name
        }
        
        if User.objects.filter(email=session_data['email']).exists():
            messages.error(request, "Email already registered")
            return render(request, "focone.html", {"show_register_modal": True})
        
        request.session.update(session_data)
        request.session['otp'] = random.randint(100000, 999999)
        
        send_mail(
            "OTP for Focone registration",
            f"Your OTP is {request.session['otp']}",
            settings.EMAIL_HOST_USER,
            [session_data['email']]
        )
        
        messages.info(request, "OTP sent to your email")
        return render(request, "focone.html", {"show_otp": True})
    
    else:
        if str(request.POST.get("otp")) == str(request.session.get('otp')):
            user = User.objects.create_user(
                first_name=request.session.get('firstname'),
                last_name=request.session.get('lastname'),
                email=request.session.get('email'),
                password =request.session.get('password'),
                phone_number="0000000000",
                no_of_focus="0"
            )
            profile_name = request.session.get('profile_picture')
            if profile_name:
             user.profile_picture = profile_name
             user.save()
               
            request.session.flush()
            return render(request, "focone.html", {"account_created": True})
        
        messages.error(request, "Incorrect OTP")
        return render(request, "focone.html", {"show_otp": True})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if not User.objects.filter(email=email).exists():
            messages.error(request, "Email not registered")
            return render(request, "focone.html", {"show_register_modal": True})
        
        user = authenticate(request, email=email, password=password)
        
        if user:
            login(request, user)
            return redirect("/")
        
        messages.error(request, "Incorrect password")
    
    return render(request, "focone.html", {"show_login_modal": request.method == "POST"})

