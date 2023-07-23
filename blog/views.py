from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from users.models import customUser
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status='PB')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)

    posts = paginator.get_page(page_number)
    context = {
        "posts" : posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, id):
    post = get_object_or_404(Post, id = id)
    context = {
        "post" : post,
    }
    return render(request, 'blog/post_detail.html', context)


def authors(request, name):
    author = customUser.objects.filter(username__exact=name)
    context = {
        'author' : author,
    }
    return render(request, 'blog/profile.html', context)

def author_posts(request, username):
    posts = Post.objects.filter(author__username__exact = username)
    context = {
        'posts' : posts
    }
    return render(request, 'blog/posts_by_author.html', context)
def label(request, label):
    posts = Post.objects.filter(category__exact=label)
    context = {
        'posts' : posts
    }
    return render(request, 'blog/posts_by_label.html', context)

# @login_required()
def send(request):
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            dbObJ = Post.objects.create(author=request.user)
            cd = form.cleaned_data
            dbObJ.title = cd['pTitle']
            dbObJ.slug = cd['pSlug']
            dbObJ.description = cd['pTXT']
            dbObJ.save()
            return redirect('blog:post_list')
    else:
        form = postForm()

    context = {
        'form' : form,
        'user' : request.user
    }
    return render(request, 'forms/send.html', context)

def logout_user(request):
    logout(request)
    return redirect('blog:post_list')