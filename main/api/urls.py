
from django.urls import path
from . import views


urlpatterns = [

    path('get_chart_reviews/', views.get_chart_reviews, name='get_chart_reviews'),
    path('get_chart_reviews_dash/', views.get_chart_reviews_dash, name='get_chart_reviews_dash'),
    path('get_chart_reviews_dash/<int:year>/', views.get_chart_reviews_dash_p, name='get_chart_reviews_dash'),
    path('get_chart_reviews/<int:year>/', views.get_chart_reviews_P, name='get_chart_reviews'),

    path('get_chart_reviews_total/', views.get_chart_reviews_total, name='get_chart_reviews_total'),
    path('get_chart_reviews_response/', views.get_chart_reviews_response, name='get_chart_reviews_response'),
    path('get_chart_reviews_stars/', views.get_chart_reviews_stars, name='get_chart_reviews_stars'),
    path('get_chart_reviews_response_nun/', views.get_chart_reviews_response_nun, name='get_chart_reviews_response_nun'),
    
]