"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('pricing/', views.pricing, name="pricing"),
    path('team/', views.team, name="team"),
    path('contact/', views.contact, name="contact"),




    path('How-it-works/', views.How_it_works, name="How-it-works"),
    path('privacy-policy/', views.privacy, name="privacy-policy"),
    path('terms-of-service/', views.terms, name="terms-of-service"),
    path('refund-policy/', views.refund, name="refund-policy"),

    path('verification-again/', views.verification_email,
         name='Verification-again'),
    path('accounts/', include('allauth.urls')),
]
