from django.contrib import admin

# Register your models here.
from .models import ContactMessage  # Import your model here

# Register your model with the admin site
admin.site.register(ContactMessage)
