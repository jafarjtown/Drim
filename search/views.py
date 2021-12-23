from accounts.models import User
from posts.models import Post, Comment
from Files.models import File
from django.db.models.query_utils import Q
from django.shortcuts import render
from itertools import chain

# Create your views here.


def Index(request):
    context = {}
    search_field = request.GET['search_input']
    result = False
    # lookup users
    users = User.objects.filter(
        Q(username__icontains = search_field)|
        Q(first_name__icontains = search_field)|
        Q(last_name__icontains = search_field)|
        Q(email__icontains = search_field)
    )
    # loolup posts
    posts = Post.objects.filter(
        Q(status__icontains = search_field)|
        Q(author__username__contains = search_field)|
        Q(author__first_name__contains = search_field)|
        Q(author__last_name__contains = search_field)|
        Q(author__email__contains = search_field)
    )
    # lookup files
    files = File.objects.filter(
        Q(name__contains = search_field)
    )
    if files or users or posts:
        result = True
    allr = [*posts,*users,*files]
    # posts['type'] = 'posts'
    print(posts)
    context['posts_result'] = posts
    context['result'] = result
    context['users_result'] = users
    context['files_result'] = files
    context['search_field'] = search_field

    return render(request, 'search/index.html', context)