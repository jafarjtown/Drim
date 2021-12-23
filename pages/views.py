from pages.models import Page
from posts.models import Post
from Files.models import File
from django.shortcuts import redirect, render

# Create your views here.
def Generate_Random_Numbers(n):
    import random as r
    number = ''
    for i in range(n):
        number += str(r.randint(0,9))
    return number

def HomePages(request):
    context = {}
    if request.method == 'POST':
        code = request.POST['code']
        pages = Page.objects.filter( verification_code = code)
        print(pages)
        print(code)
        context['pages'] = pages
    return render(request, 'pages/pages.html', context)
def HomePagesName(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        pages = Page.objects.filter( name = name)
        context['pages'] = pages
    return render(request, 'pages/pages.html', context)
def CreatePage(request):
    context = {}
    user = request.user
    if request.method == 'POST':
        message = ''
        page_info = request.POST
        print(page_info)
        page = Page.objects.create(name = page_info['name'], about=page_info['about'], website_url=page_info['website_url'])
        print(dir(user))
        if user.is_authenticated:
            page.verification_code = Generate_Random_Numbers(15)
            page.admins.add(user)
            page.followers.add(user)
        else:
            page.verification_code = Generate_Random_Numbers(15)
            message = f'Login and use this [{page.verification_code} ] as code to be admin to this [ {page.name} ] page...'
            
            context['message'] = message
        page.save()
        
    return render(request, 'pages/page.create.html', context)
def HomePage(request,name,id):
    context = {}
    page = Page.objects.get(id = id)
    context['page'] = page
    if request.method == 'POST':
        status = request.POST.get('status')
        medias = request.FILES.getlist('medias')
        user = request.user
        post = Post.objects.create(author = user, status = status)
        if len(medias) > 0:
            for f in medias:
                f = File.objects.create(file = f, name=status[0:10])
                post.files.add(f)
        page.posts.add(post)
    return render(request, 'pages/pages.home.html', context)
def VerficationPage(request,name,id):
    context = {}
    page = Page.objects.get(id = id)
    if request.user in page.admins:
        return redirect('pages:home-page', name, id)
    if request.method == 'POST':
        message = ''
        code = request.POST['code']
        if page.verification_code == code:
            page.admins.add(request.user)
            page.followers.add(request.user)
        else:
            message = f'wrong verification code... please retry again..'
            context['message'] = message
    return render(request,'pages/page.admins.html', context)
# print(Generate_Random_Numbers(10))
def FollowUnfollowPage(request, pgi):
    page = Page.objects.get(id = pgi)
    user = request.user
    if user in page.followers.all():
        page.followers.remove(user)
    else:
        page.followers.add(user)
    page.save()
    print('follow')
    return redirect('home-page', page.name, page.id)