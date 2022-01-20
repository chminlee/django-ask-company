from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model) : 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(blank=False)
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta : 
        ordering = ['id']

    def __str__(self) -> str : 
        return self.message

    def message_length(self) -> int : 
        return len(self.message)

    message_length.short_description = 'lenth of message'

class Comment(models.Model) : 
    post = models.ForeignKey("instagram.Post", on_delete=models.CASCADE) # post_id 필드가 생성이 됨
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)