from django.contrib import admin
from .models import Profile

# Registers the Profile model to be accessible in the admin page
admin.site.register(Profile)
