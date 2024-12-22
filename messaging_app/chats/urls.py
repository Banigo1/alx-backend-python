# chats/urls.py

from django.urls import path
from .views import ConversationListView, MessageListView

urlpatterns = [
    path('conversations/', ConversationListView.as_view(), name='conversation-list'),
    path('messages/', MessageListView.as_view(), name='message-list'),
]
