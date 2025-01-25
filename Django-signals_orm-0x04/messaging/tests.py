from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class MessageNotificationTest(TestCase):

    def setUp(self):
        """Create users for testing."""
        self.sender = User.objects.create(username='sender')
        self.receiver = User.objects.create(username='receiver')

    def test_notification_created_on_message_send(self):
        """Test that a notification is created when a new message is sent."""
        message = Message.objects.create(sender=self.sender, receiver=self.receiver, content='Hello!')
        
        # Check if notification was created
        notification_exists = Notification.objects.filter(user=self.receiver, message=message).exists()
        self.assertTrue(notification_exists)

        # Check the content of the notification
        notification = Notification.objects.get(user=self.receiver, message=message)
        self.assertEqual(notification.message.content, 'Hello!')
