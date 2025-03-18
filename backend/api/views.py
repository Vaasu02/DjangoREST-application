# Import render function from Django (for rendering templates, though not used here)
from django.shortcuts import render
# Import generic API views from Django REST Framework - these provide pre-built view functionality
from rest_framework import generics
# Import our UserSerializer that we created in serializers.py
from .serializers import UserSerializer,NoteSerializer
# Import Django's built-in User model
from django.contrib.auth.models import User
# Import permission classes to control who can access our API
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Note


# Create a view for handling user registration
# CreateAPIView provides POST method for creating users
class CreateUserView(generics.CreateAPIView):
    # Specify which database objects are available to this view (all users)
    queryset = User.objects.all()
    # Specify which serializer to use for converting data
    serializer_class = UserSerializer
    # Allow anyone to access this view (necessary for registration)
    permission_classes = [AllowAny]

# Create a view for handling note creation
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user=self.request.user # get the current logged in user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
            print("serializer is not valid")

# Create a view for handling note  deletions
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)
