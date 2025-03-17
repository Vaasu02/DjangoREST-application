from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # ForeignKey establishes a many-to-one relationship with User model
    # on_delete=CASCADE means if user is deleted, their notes will also be deleted
    # related_name allows reverse lookup of notes from user instance via user.notes
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='notes')
    
    def __str__(self):
        return self.title
