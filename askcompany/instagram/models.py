from django.db import models

# Create your models here.
class Post(models.Model) : 
    message = models.TextField(blank=False)
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str : 
        return self.message

    def message_length(self) -> int : 
        return len(self.message)

    message_length.short_description = 'lenth of message'