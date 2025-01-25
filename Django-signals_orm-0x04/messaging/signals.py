from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory
from django.db import models

@receiver(post_delete, sender=User)
def delete_related_data(sender, instance, **kwargs):
    # Delete all messages associated with the user
    Message.objects.filter(user=instance).delete()

    # Delete all notifications associated with the user
    Notification.objects.filter(user=instance).delete()

    # Delete all message histories associated with the user
    MessageHistory.objects.filter(user=instance).delete()

class MessageHistory(models.Model):
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    action = models.CharField(max_length=10)  # e.g., 'created', 'updated'
    timestamp = models.DateTimeField(auto_now_add=True)