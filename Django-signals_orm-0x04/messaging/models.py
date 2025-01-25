from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Message

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    read = models.BooleanField(default=False)  # New field to track read status
    created_at = models.DateTimeField(auto_now_add=True)# Tracks if the message has been edited

    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}{'...' if len(self.content) > 30 else ''}"

def inbox_view(request):
    unread_messages = Message.unread_objects.for_user(request.user)
    return render(request, 'inbox.html', {'unread_messages': unread_messages})

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()  # Default manager
    unread_objects = UnreadMessagesManager()  # Custom manager for unread messages


class UnreadMessagesManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user, read=False).only('id', 'content', 'created_at')  # Optimize query

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="history")
    old_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for message {self.message.id}"

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # Check if this is an update (not a new instance)
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:  # Content has changed
                MessageHistory.objects.create(message=old_message, old_content=old_message.content)
                instance.edited = True  # Mark the message as edited
        except Message.DoesNotExist:
            pass
