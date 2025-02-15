from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Message
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

@cache_page(60)  # Cache the view for 60 seconds
def conversation_messages(request, conversation_id):
    messages = Message.objects.filter(conversation_id=conversation_id).order_by('timestamp')
    return render(request, 'conversation_messages.html', {'messages': messages})


class UserMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch messages for the authenticated user
        user = request.user
        messages = user.messages.all()  # Assuming a related name 'messages'
        return Response({'messages': [message.content for message in messages]})
