# chats/urls.py

from django.urls import path, include
from .views import ConversationListView, MessageListView
from rest_framework.routers import DefaultRouter
from . import views


# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'conversations', views.ConversationViewSet, basename='conversation')
router.register(r'messages', views.MessageViewSet, basename='message')

# URL Patterns
urlpatterns = [
    path('', include(router.urls)),  # Include the router-generated URLs
]

""" Explanation of Key Components
include:
Used to include the router-generated URLs in the main URL patterns.
routers.DefaultRouter():

Automatically creates RESTful API endpoints (e.g., /users/, /conversations/, /messages/).
router.register():

Registers viewsets to generate URLs for CRUD operations.
Example ViewSets: If you haven’t already created viewsets, here are examples for User, Conversation, and Message:
"""