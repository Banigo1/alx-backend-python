# chats/serializers.py

from rest_framework import serializers
from .models import CustomUser, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'profile_picture']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'created_at', 'updated_at']


class MessageSerializer(serializers.ModelSerializer):
    conversation_id = serializers.CharField(source='conversation.id', read_only=True)
    sender_username = serializers.CharField(source='sender.username', read_only=True)
    time_sent = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = [
            'message_id',
            'conversation_id',
            'sender_username',
            'message_body',
            'time_sent',
            'sent_at',
        ]

    def get_time_sent(self, obj):
        return obj.sent_at.strftime('%Y-%m-%d %H:%M:%S')

    def validate_message_body(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Message body cannot be empty.")
        return value
