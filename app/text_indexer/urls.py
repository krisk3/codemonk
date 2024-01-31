"""
URL configuration for app project.
"""
from django.urls import path
from .views import AddTextView, SearchWordView

# Define the URL patterns for the text_indexer app
urlpatterns = [
    # URL pattern for adding text using AddTextView
    path("add-text/", AddTextView.as_view(), name="add_text"),
    # URL pattern for searching a word using SearchWordView
    path("search-word/", SearchWordView.as_view(), name="search_word"),
]
