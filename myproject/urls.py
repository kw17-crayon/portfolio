"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import myapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name="home"),
    path('mypage/', myapp.views.mypage, name="mypage"),
    path('incollege/', myapp.views.incollege, name="incollege"),
    path('myproject/', myapp.views.myproject, name="myproject"),
    path('contact/', myapp.views.contact, name="contact"),
    path('myproject/inproject/', myapp.views.INPROJECT, name="INPROJECT"),
    path('incollege/grade1', myapp.views._grade, name="grade1"),
]
