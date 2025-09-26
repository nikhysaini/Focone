from django.shortcuts import render , redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import random


def index(request):
    return render(request,"focone.html")

def register_view(request):
    if request.method == "POST" and not request.POST.get("otp"):
        request.session['firstname'] = request.POST.get("firstname")
        request.session['lastname'] = request.POST.get("lastname")
        request.session['email'] = request.POST.get("email")
        request.session['password'] = request.POST.get("password")
        request.session['username'] = request.session.get('email') 

        if User.objects.filter(email=request.session.get('email')).exists():
            request.session.flush()
            messages.error(request,"Email is already registered. Please choose another")
            return render(request, "focone.html", {"show_register_modal": True})

        request.session['otp'] = random.randint(100000, 999999) 
        otp = request.session.get('otp')
        subject = "OTP for Focone registration"
        message = f"Your OTP for registration is {otp}"
        send_mail(subject,message,settings.EMAIL_HOST_USER,[request.session.get('email')])

        messages.error(request,"OTP sent to registered email")
        return render(request, "focone.html", { "show_otp": True})

    if request.method == "POST" and request.POST.get("otp"):
        user_opt = request.POST.get("otp")
        if str(user_opt) == str(request.session.get('otp')):
            user = User.objects.create(
                first_name=request.session.get('firstname'),
                last_name=request.session.get('lastname'),
                username=request.session.get('username'),
                email=request.session.get('email')
            )
            user.set_password(request.session.get('password'))
            user.save()
            request.session.flush()
            return render(request, "focone.html", {"account_created":True})
        else:
            messages.error(request,"Incorrect otp")
            return render(request, "focone.html", {"show_otp":True})

    return render(request,"focone.html")

def login_view(request):
    if request.method == "POST":
      email= request.POST.get("email")
      password = request.POST.get("password")
      if not User.objects.filter(email=email).exists():
          messages.error(request,"Email not register")
          return render(request, "focone.html", {"show_register_modal": True})
      
      user = authenticate(username=email,password=password)
      
      if not user:
        messages.error(request,"Incorrect password")
        return render(request, "focone.html", {"show_login_modal": True})
    
      login(request,user)
      messages.success(request,"Login successfully")
      return redirect("/")
    return redirect("/")
      

