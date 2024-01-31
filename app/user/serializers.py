"""
Django serializers for handling data serialization and deserialization.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user object.

    This serializer is used to convert complex data types, such as Django models,
    into Python data types that can be easily rendered into JSON and vice versa.
    """

    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "password",
            "name",
            "dob",
        ]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """
        Create and return a user with encrypted password.

        This method is responsible for creating a new user object with the provided
        validated data. It ensures that the user's password is encrypted before
        saving it to the database.
        """
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """
    Serializer for the user auth token.

    This serializer is used for handling authentication tokens. It takes email
    and password as input and performs user authentication.
    """

    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """
        Validate and authenticate the user.

        This method validates the provided email and password and attempts to
        authenticate the user. If the authentication is successful, it returns
        the validated attributes including the user object. Otherwise, it raises
        a validation error with a corresponding message.
        """
        email = attrs.get("email")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password,
        )
        if not user:
            msg = _("Unable to authenticate with provided credentials.")
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs
