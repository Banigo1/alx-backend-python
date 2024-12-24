from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import filters
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer
from rest_framework import generics

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']  # Search users by username or email

# Conversation ViewSet
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'updated_at']  # Allow ordering by creation and update times
    ordering = ['created_at']  # Default ordering by creation date

    # You can add custom actions like creating conversations for specific users
    def create(self, request, *args, **kwargs):
        # Custom logic to create a conversation, if necessary
        return super().create(request, *args, **kwargs)

# Message ViewSet
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['sent_at']
    search_fields = ['message_body']  # Allow search by message body
    ordering = ['sent_at']  # Default ordering by sent date

    def create(self, request, *args, **kwargs):
        # Custom logic to create a message, if necessary
        return super().create(request, *args, **kwargs)
    
    

"""Explanation of Key Components
viewsets.ModelViewSet:

We are using ModelViewSet, which provides the full CRUD functionality out of the box for our models (User, Conversation, Message).
status:

This is used for returning HTTP status codes. In the provided code, it’s imported, but we haven't explicitly used it in the default ModelViewSet implementation. You might use status if you need custom response codes, e.g., Response(data, status=status.HTTP_400_BAD_REQUEST).
filters:

We are using DRF’s filters to allow searching and ordering:
filters.SearchFilter: Allows searching across specific fields like username for User and message_body for Message.
filters.OrderingFilter: Allows clients to order the results by fields like created_at and sent_at.
ConversationViewSet:

This handles conversations. We added custom ordering logic so users can order conversations by created_at and updated_at. You can also customize create if needed.
MessageViewSet:

This manages messages. It supports both search and ordering functionality, allowing filtering messages by message_body and ordering by sent_at.
"""

class UserMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(user=self.request.user)
