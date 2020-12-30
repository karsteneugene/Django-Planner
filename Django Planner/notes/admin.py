from django.contrib import admin
from .models import Note

# Registers the Note model to be accessible in the admin page
admin.site.register(Note)
