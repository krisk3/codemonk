"""
URL configuration for app project.
"""
from django.urls import path
from user import views

# Define the app namespace for URL reverse lookup
app_name = "user"

# Define the URL patterns for the user app
urlpatterns = [
    # URL pattern for creating a new user
    path("create/", views.CreateUserView.as_view(), name="create"),
    # URL pattern for generating an authentication token
    path("token/", views.CreateTokenView.as_view(), name="token"),
]
