from .models import Profile
from django.contrib import admin

# Register your models here.
@admin.register(Profile)
class ProgileAdmin(admin.ModelAdmin) : 
    list_display = ["user", "address", "zip_code"]