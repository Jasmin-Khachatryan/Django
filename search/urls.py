from django.urls import path
from search.views import AdvancedSearchView

urlpatterns = [

    path("", AdvancedSearchView.as_view(), name="search"),
]
