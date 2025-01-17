from datetime import datetime
import logging
from django.http import HttpResponse
from django.core.cache import cache
import time

# Configure logging
logging.basicConfig(
    filename='requests.log',
    level=logging.INFO,
    format='%(message)s'
)

""" Each middleware implements specific functionality:

** RequestLoggingMiddleware:

Logs all requests to requests.log
Includes timestamp, username, and request path
Creates log file automatically


** RestrictAccessByTimeMiddleware:

Restricts access to the chat between 9 AM and 6 PM
Returns 403 Forbidden outside these hours


** RateThrottlingMiddleware:

Limits users to 5 messages per minute
Uses IP address to track users
Uses Django's cache framework for tracking
Returns 429 Too Many Requests when limit exceeded


** RolePermissionMiddleware:

Checks if user is admin or moderator
Returns 403 Forbidden if user lacks proper permissions

"""

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get username or 'Anonymous' if user is not authenticated
        user = request.user.username if request.user.is_authenticated else 'Anonymous'
        
        # Log the request
        logging.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        
        return self.get_response(request)

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        
        # Allow access only between 9 AM and 6 PM
        if current_hour < 9 or current_hour > 18:
            return HttpResponse('Access denied. Chat is only available between 9 AM and 6 PM.', 
                              status=403)
        
        return self.get_response(request)

class RateThrottlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = 5  # messages per minute
        self.time_window = 60  # seconds

    def __call__(self, request):
        if request.method == 'POST' and 'chats' in request.path:
            client_ip = request.META.get('REMOTE_ADDR')
            cache_key = f'rate_limit_{client_ip}'
            
            # Get current count and timestamp
            current_data = cache.get(cache_key, {'count': 0, 'timestamp': time.time()})
            
            # Reset counter if time window has passed
            if time.time() - current_data['timestamp'] > self.time_window:
                current_data = {'count': 0, 'timestamp': time.time()}
            
            # Increment counter
            current_data['count'] += 1
            
            # Check if rate limit exceeded
            if current_data['count'] > self.rate_limit:
                return HttpResponse('Rate limit exceeded. Please wait before sending more messages.',
                                  status=429)
            
            # Update cache
            cache.set(cache_key, current_data, self.time_window)
        
        return self.get_response(request)

class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Check if user has admin or moderator role
            is_admin = request.user.is_staff or request.user.is_superuser
            is_moderator = request.user.groups.filter(name='moderator').exists()
            
            if not (is_admin or is_moderator):
                return HttpResponse('Access denied. Insufficient permissions.',
                                  status=403)
        
        return self.get_response(request)