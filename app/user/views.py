"""
Django views for handling HTTP requests and rendering responses.
"""
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from django.contrib.auth import get_user_model

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(APIView):
    """
    API view for creating a new user in the system.

    Handles HTTP POST requests with user data to create a new user.

    Attributes:
        serializer_class (class): The serializer class used for validating and
                                 processing incoming user data.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to create a new user.

        Args:
            request (Request): The HTTP request object.
            *args: Variable-length argument list.
            **kwargs: Variable-length keyword argument list.

        Returns:
            Response: HTTP response with user data and token on success,
                      or error messages on failure.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = get_user_model().objects.create_user(**serializer.validated_data)
            print(serializer.data)
            token, _ = Token.objects.get_or_create(user=user)
            val = {"user": serializer.data, "token": token.key}
            return Response(val, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
