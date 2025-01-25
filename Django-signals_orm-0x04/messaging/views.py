from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Message

@cache_page(60)  # Cache the view for 60 seconds
def conversation_messages(request, conversation_id):
    messages = Message.objects.filter(conversation_id=conversation_id).order_by('timestamp')
    return render(request, 'conversation_messages.html', {'messages': messages})
