"""
URL configuration for messaging_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# messaging_app/urls.py

from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a Default Router for the main resources
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'conversations', views.ConversationViewSet, basename='conversation')
router.register(r'messages', views.MessageViewSet, basename='message')

# URL Patterns
urlpatterns = [
    path('', include(router.urls)),  # Include the main router URLs
    path('api-auth/', include('rest_framework.urls')),  # Add this line to include api-auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/messages/', UserMessagesView.as_view(), name='user_messages'),
]
