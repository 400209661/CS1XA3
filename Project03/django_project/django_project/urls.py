"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib,auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('e/antemiaa/admin/', admin.site.urls),
    path('e/antemiaa/register/', user_views.register, name ='register'),
    path('e/antemiaa/login/', auth_views.LoginView.as_view(template_name= 'Users/login.html'), name ='login'),
    path('e/antemiaa/logout/', auth_views.LogoutView.as_view(template_name= 'Users/logout.html'), name ='logout'),
    path('e/antemiaa/', include('simon.urls'))
]
