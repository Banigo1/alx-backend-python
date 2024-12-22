# chats/serializers.py

from rest_framework import serializers
from .models import CustomUser, Conversation, Message

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number']

class ConversationSerializer(serializers.ModelSerializer):
    messages = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'messages', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()  # Or use PrimaryKeyRelatedField if needed

    class Meta:
        model = Message
        fields = ['id', 'sender', 'conversation', 'content', 'timestamp']
