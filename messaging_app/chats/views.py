# chats/views.py

from rest_framework import generics
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from django.http import HttpResponse

class ConversationListView(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

def home(request):
    return HttpResponse("<h1>Welcome to the Messaging App!</h1>")
