from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 
import uuid  # Import UUID for unique identifier generation

class User(models.Model):
    """
    Model representing a user in the messaging system.
    """
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# User Model extending AbstractUser
class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # Example custom field
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.username



class CustomUser(AbstractUser):
    # Add any additional fields here
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # You can add more fields as needed

    def __str__(self):
        return self.username

# Conversation Model
class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        participant_usernames = ', '.join([user.username for user in self.participants.all()])
        return f"Conversation ({participant_usernames})"
    
    
# Message Model
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name='messages', db_column='conversation_id'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message by {self.sender.username} in Conversation {self.conversation.id}"


# chats/models.py

class CustomUser(models.Model):
    # Your custom user fields here
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)