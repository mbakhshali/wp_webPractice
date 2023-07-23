import re
from django import template
from users.models import customUser

import users.models
from ..models import Post
from django.contrib.auth.models import User
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('parts/sidebar_latest.html')
def sidebar_latest(cnt=5):
    # l_s = Post.objects.all()[:cnt]
    l_s = Post.objects.filter(status='PB')[:cnt]
    context = {
        'l_s' : l_s
    }
    return context

@register.filter(name='censore')
def s(text):
    banned = ['khar', 'gav', 'olagh']
    result = [word for word in re.split('\W+', text)]

    for i in result:
        if i in banned:
            text = text.replace(i, '*'*len(i))

    return text
@register.simple_tag()
def count():
    return Post.objects.filter(status='PB').count()

@register.simple_tag()
def user_postz():
    result = customUser.objects.filter(user_posts__status='PB').annotate(userMax = Count('user_posts')).order_by('-userMax')
    return result[0]