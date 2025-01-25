from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Notification

@receiver(post_save, sender=Message)
def notify_user(sender, instance, created, **kwargs):
    """Creates a notification when a new message is sent."""
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)
        print(f'Notification: New message from {instance.sender.username} to {instance.receiver.username}')
