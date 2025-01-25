# Django-Chat/Views.py

from django.shortcuts import render, get_object_or_404
from .Models import Message

def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    history = message.history.all()  # Fetch related MessageHistory objects
    return render(request, "message_detail.html", {"message": message, "history": history})
