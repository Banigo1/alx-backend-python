from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(models.Model):
    """Represents a user in the system."""
    username = models.CharField(max_length=100)
    email = models.EmailField()

class Message(models.Model):
    """Represents a message sent from one user to another."""
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}'

class Notification(models.Model):
    """Represents a notification for a user regarding new messages."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)