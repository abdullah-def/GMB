"""
Application URLs
"""
from django.urls import path

from .views import (
    ArticleIndexView, ArticleDetailView,
    AuthorIndexView, AuthorDetailView,
    CategoryIndexView, CategoryDetailView,
    PreviewTogglerView, PreviewArticleDetailView,
    TagIndexView, TagDetailView, TagAutocompleteView,
)


app_name = "lotus"


urlpatterns = [
    path("", ArticleIndexView.as_view(), name="article-index"),


    path(
        "categories/<slug:slug>/",
        CategoryDetailView.as_view(),
        name="category-detail"
    ),
   
    path("tags/", TagIndexView.as_view(), name="tag-index"),
    path(
        "tags/autocomplete/",
        TagAutocompleteView.as_view(),
        name="tag-autocomplete",
    ),


    #############################
    path(
        "tags/<str:tag>/",
        TagDetailView.as_view(),
        name="tag-detail"
    ),

    path(
        "<int:year>/<int:month>/<int:day>/<slug:slug>/",
        ArticleDetailView.as_view(),
        name="article-detail"
    ),
]
