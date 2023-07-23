from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>', views.post_detail, name='post_detail'),
    path('author/<str:name>', views.authors, name='post_author'),
    path('label/<str:label>', views.label, name='post_label'),
    path('send/', views.send, name='post_send'),
    path('logout/', views.logout_user, name='logout'),
    path('posts_by/<str:username>', views.author_posts, name='all author posts')
]