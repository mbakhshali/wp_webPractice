from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    ordering = ['-publish']
    search_fields = ['title', 'description']
    prepopulated_fields = {
        'slug' : ['title']
    }
    list_editable = ['status']