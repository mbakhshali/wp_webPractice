from django.urls import path
from . import views

urlpatterns = [
    path('', views.text2pic, name= 'text2pic'),
]
