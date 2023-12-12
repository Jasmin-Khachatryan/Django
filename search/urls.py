from django.urls import path
from search.views import advanced_search

urlpatterns = [

    path("", advanced_search, name="search"),
]
