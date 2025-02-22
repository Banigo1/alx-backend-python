from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet, DeleteUserView, ThreadedConversationView
from .views import UnreadMessagesView

router = DefaultRouter()
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
    path('delete-account/', DeleteUserView.as_view(), name='delete_account'),
    path('conversations/<int:conversation_id>/', ThreadedConversationView.as_view(), name='threaded_conversation'),
    path('messages/unread/', UnreadMessagesView.as_view(), name='unread_messages'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('conversation/<int:message_id>/', views.conversation_view, name='conversation_view'),
    path('unread/', unread_messages, name='unread_messages'),
]
