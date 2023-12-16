from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.home, name="app"),
    path('notifications/', views.notifications, name="notifications"),
    path('accounts/', views.accounts, name="accounts"),
    path('profile/', views.profile, name="profile"),
    path('profile_edit/', views.profile_edit_page, name="profile_edit_page"),
    
    path('reviews/', views.reviews, name="reviews"),
    path('plans/', views.plans, name="plans"),
    path('settings/', views.settings, name="settings"),

    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('settings/edit', views.settings_edit, name='settings_edit'),



]
