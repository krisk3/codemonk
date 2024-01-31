from django.urls import path
from .views import AddTextView, SearchWordView

urlpatterns = [
    path('add-text/', AddTextView.as_view(), name='add_text'),
    path('search-word/', SearchWordView.as_view(), name='search_word'),
]

