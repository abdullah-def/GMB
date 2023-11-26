from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.home, name="app"),
    path('settings/', views.settings, name="settings"),
    path('profile/', views.profile, name="profile"),
    path('plans/', views.plans, name="plans"),
    path('reviews/', views.reviews, name="reviews"),
    path('accounts/', views.accounts, name="accounts"),

    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('settings/edit', views.settings_edit, name='settings_edit'),



]
