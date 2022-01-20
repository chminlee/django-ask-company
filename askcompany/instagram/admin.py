from django.contrib import admin

# Register your models here.
from typing import Optional
from django.utils.safestring import mark_safe
from .models import Comment, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin) : 
    list_display = ["id", "message", "message_length", "created_at", "updated_at"]
    list_display_links = ["message"]
    list_filter = ["created_at", "is_public"]
    search_fields = ['message']

    def photo_tag(self, post: Post) -> Optional[str] : 
        if post.photo : 
            return mark_safe(f'<img src="{post.photo.url}" style="wudth: 75" />')
        return None
    
    def message_length(self, post: Post) -> str : 
        return f"{len(post.message)} 글자"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin) : 
    pass