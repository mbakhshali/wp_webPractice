from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator

# Create your views here.

# def post_list_s(request):
#     posts_raw = Post.objects.all()
#     context = {
#         "posts_raw" : posts_raw
#     }
#     return render(context)

def post_list(request):
    posts_raw = Post.objects.all()[:5]
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)

    posts = paginator.get_page(page_number)
    context = {
        "posts" : posts,
        "posts_raw" : posts_raw
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, id = id)
    context = {
        "post" : post
    }
    return render(request, 'blog/post_detail.html', context)