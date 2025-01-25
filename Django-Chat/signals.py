from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Message, MessageHistory

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    """Logs the old content of a message before it is edited."""
    if instance.pk:  # Check if the message already exists
        old_instance = Message.objects.get(pk=instance.pk)
        if old_instance.content != instance.content:
            MessageHistory.objects.create(message=old_instance, old_content=old_instance.content)
            instance.edited = True  # Mark as edited
