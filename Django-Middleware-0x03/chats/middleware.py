from datetime import datetime
import logging
from django.http import HttpResponse
from django.core.cache import cache
import time

""" Each middleware implements specific functionality:

** RequestLoggingMiddleware
----------------------------------
Logs all requests to requests.log
Includes timestamp, username, and request path
Creates log file automatically


** RestrictAccessByTimeMiddleware:
----------------------------------
Restricts access to the chat between 9 AM and 6 PM
Returns 403 Forbidden outside these hours


** RateThrottlingMiddleware:
----------------------------------
Limits users to 5 messages per minute
Uses IP address to track users
Uses Django's cache framework for tracking
Returns 429 Too Many Requests when limit exceeded


** RolePermissionMiddleware:
----------------------------------
Checks if user is admin or moderator
Returns 403 Forbidden if user lacks proper permissions

"""

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Extract user and request path information
        user = request.user if request.user.is_authenticated else "Anonymous"
        path = request.path

        # Log the information to a file
        log_message = f"{datetime.datetime.now()} - User: {user} - Path: {path}\n"
        with open("request_logs.txt", "a") as log_file:
            log_file.write(log_message)

        # Call the next middleware or view
        response = self.get_response(request)
        return response

#_________________________________________________________________________________________________

# 3. Detect and Block offensive Language

import time
from collections import defaultdict
from django.http import JsonResponse

class OffensiveLanguageMiddleware:
    """
    Middleware to limit the number of chat messages a user can send within a certain time window,
    based on their IP address. This helps prevent spam and excessive messaging.

    Features:
    - Tracks the number of POST requests (messages) from each IP address.
    - Implements a time-based limit (e.g., 5 messages per minute).
    - Blocks further messaging if a user exceeds the limit and returns an error response.

    Attributes:
        get_response (callable): The next middleware or view to handle the request.
        message_log (defaultdict): A dictionary to log timestamps of messages by IP address.
        limit (int): The maximum number of messages allowed within the time window.
        time_window (int): The duration of the time window in seconds.
    """

    def __init__(self, get_response):
        """
        Initializes the middleware with the given response handler.

        Args:
            get_response (callable): The next middleware or view to handle the request.
        """
        self.get_response = get_response
        self.message_log = defaultdict(list)  # Tracks timestamps of messages by IP address
        self.limit = 5  # Number of allowed messages
        self.time_window = 60  # Time window in seconds (1 minute)

    def __call__(self, request):
        """
        Processes incoming requests and enforces the message limit for POST requests.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The HTTP response to the request. If the message limit is exceeded,
            returns a 429 Too Many Requests error with a JSON error message.
        """
        if request.method == 'POST':
            ip_address = self.get_client_ip(request)
            current_time = time.time()

            # Filter out timestamps outside the time window
            self.message_log[ip_address] = [
                timestamp for timestamp in self.message_log[ip_address] 
                if current_time - timestamp < self.time_window
            ]

            # Check if the user exceeds the limit
            if len(self.message_log[ip_address]) >= self.limit:
                return JsonResponse(
                    {"error": "Message limit exceeded. Please try again later."}, 
                    status=429
                )

            # Log the current message timestamp
            self.message_log[ip_address].append(current_time)

        response = self.get_response(request)
        return response

    @staticmethod
    def get_client_ip(request):
        """
        Retrieves the IP address of the client from the HTTP request.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            str: The IP address of the client.
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

#_____________________________________________________________________________________________

# 4. Enforce chat user Role Permissions

from django.http import JsonResponse

class RolePermissionMiddleware:
    """
    Middleware to restrict access based on user roles. Only users with roles 'admin' or 'moderator'
    are allowed to proceed.

    If the user's role is not 'admin' or 'moderator', a 403 Forbidden error is returned.

    Attributes:
        get_response (callable): The next middleware or view to handle the request.
    """

    def __init__(self, get_response):
        """
        Initializes the middleware with the given response handler.

        Args:
            get_response (callable): The next middleware or view to handle the request.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Processes incoming requests and checks the user's role.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The HTTP response to the request. If the user is not authorized, 
            a 403 Forbidden error is returned.
        """
        user_role = request.META.get('HTTP_USER_ROLE')  # Assuming role is sent in request headers

        if user_role not in ('admin', 'moderator'):
            return JsonResponse(
                {"error": "Forbidden: You do not have permission to access this resource."}, 
                status=403
            )

        response = self.get_response(request)
        return response
