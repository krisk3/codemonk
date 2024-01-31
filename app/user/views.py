"""
Django views for handling HTTP requests and rendering responses.
"""
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """
    View for creating a new user in the system.

    This view allows clients to send a POST request with user data
    to create a new user in the system.

    Attributes:
        serializer_class: The serializer class used for validating and
                          processing incoming user data.
    """

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """
    View for creating a new authentication token for a user.

    This view extends the ObtainAuthToken view from the rest_framework
    module and adds the ability to create a new authentication token
    for a user by sending a POST request with valid credentials.

    Attributes:
        serializer_class: The serializer class used for validating and
                          processing incoming authentication token data.
        renderer_classes: The renderer classes used for rendering the
                          response data. Defaults to the default renderer
                          classes specified in the API settings.
    """

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
