"""
URL configuration for focone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.index, name='index'),
   path('login/', views.login_view, name='login'),  
   path('edit-profile/', views.editprofile, name='editprofile'), 
   path('profile/', views.profile, name='profile'), 
   path('focus-mode/', views.focusmode, name='focusmode'), 
   path('register/', views.register_view, name='register'),
   path('otp/', views.register_view, name='otp'), 
   path('admin/', admin.site.urls), 
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   