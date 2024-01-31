"""
Define admin classes for managing models in the Django admin interface.
"""
from django.contrib import admin
from text_indexer import models

# Register the Paragraph model with the admin site using the custom admin configuration
admin.site.register(models.Paragraph)

# Register the Word model with the admin site using the custom admin configuration
admin.site.register(models.Word)
