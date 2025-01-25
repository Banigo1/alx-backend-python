from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Message # the Message model

@cache_page(60)  # Cache the view for 60 seconds
def conversation_messages(request, conversation_id):
    messages = Message.objects.filter(conversation_id=conversation_id).order_by('timestamp')
    return render(request, 'conversation_messages.html', {'messages': messages})

def inbox_view(request):
    # Retrieve unread messages for the logged-in user with optimized query
    unread_messages = Message.unread_objects.for_user(request.user).only('id', 'content', 'created_at')
    
    # Render the inbox template with the unread messages
    return render(request, 'inbox.html', {'unread_messages': unread_messages})


def unread_messages(request):
    if request.user.is_authenticated:
        # Fetch unread messages for the logged-in user
        unread_messages = Message.unread.unread_for_user(request.user).select_related('sender', 'recipient')
        return render(request, 'unread_messages.html', {'messages': unread_messages})
    else:
        return render(request, 'error.html', {'message': 'You need to log in to see your messages.'})

