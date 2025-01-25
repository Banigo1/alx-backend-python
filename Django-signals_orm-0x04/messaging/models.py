from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class MessageHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_histories')
    history = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
