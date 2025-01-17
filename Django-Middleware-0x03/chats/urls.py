# chats/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter  # Import the nested router
from . import views

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'conversations', views.ConversationViewSet, basename='conversation')
router.register(r'messages', views.MessageViewSet, basename='message')

# Create a Nested Default Router for nested routes (e.g., messages within a conversation)
conversation_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversation_router.register(r'messages', views.MessageViewSet, basename='conversation-messages')

# URL Patterns
urlpatterns = [
    path('', include(router.urls)),  # Include the main router URLs
    path('', include(conversation_router.urls)),  # Include the nested router URLs
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