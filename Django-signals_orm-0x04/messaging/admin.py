from django.contrib import admin
from .models import Message, MessageHistory

# Allow users to view previous versions of their messages in the admin interface.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp', 'edited')

@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('message', 'old_content', 'edited_at')
