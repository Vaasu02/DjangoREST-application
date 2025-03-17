# Import Django's built-in User model - this is what we'll be working with
from django.contrib.auth.models import User
# Import serializers from Django REST Framework - these help convert Python objects to JSON and vice versa
from rest_framework import serializers
from .models import Note

# Create a serializer class for User model - this will handle converting User data to/from JSON
class UserSerializer(serializers.ModelSerializer):
    # Meta class defines the configuration for our serializer
    class Meta:
        # Specify which model to serialize
        model = User
        # List which fields we want to include when converting to/from JSON
        fields = ['id', 'username', 'password']
        # Special settings: make password write-only for security (won't be visible in API responses)
        extra_kwargs = {'password': {'write_only': True}}

    # Custom method to handle user creation
    def create(self, validated_data):
        # Create a new user with the validated data, properly hashing the password
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        # Return the newly created user object
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'author']
        # by this we are making author field read only so that user can't change the author of the note
        extra_kwargs = {'author': {'read_only': True}}

           