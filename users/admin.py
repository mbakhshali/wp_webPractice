from django.contrib import admin
from .models import customUser


# Register your models here.
@admin.register(customUser)
class userAdmin(admin.ModelAdmin):
    list_display = ['email']