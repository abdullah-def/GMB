from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.home, name="app"),
    path('notifications/', views.notifications, name="notifications"),
    path('accounts/', views.accounts, name="accounts"),
    path('profile/', views.profile, name="profile"),
    path('profile_edit/', views.profile_edit_page, name="profile_edit_page"),
    
    path('reviews_list/', views.reviews_list, name="reviews_list"),
    path('reviews_analysis/', views.reviews_analysis, name="reviews_analysis"),
    path('business_details/', views.business_details, name="business_details"),
    path('plans/', views.plans, name="plans"),
    path('settings/', views.settings, name="settings"),

    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('settings/edit', views.settings_edit, name='settings_edit'),



]
