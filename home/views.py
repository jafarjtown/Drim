from django.db.models.query_utils import Q
from institution.models import Institution
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from posts.models import Post, Story
from accounts.models import Student, User
from notifications.notifcations import PostNotification
from django.core.paginator import Paginator
from Files.models import File
from django.utils import timezone
import time
# Create your views here.
def Escape(string):
    import re
    def escapeword(string):
        fs = string[0].split('>')[0] + '>'
        ls = '<'
        ls += string[0].split('<')[-1]
        print(fs[0:-1],ls[0:-1])
        
        st = string[0].split('>')[1].split('<')[0]
        print(f'&lt{fs[1:-1]}&gt{st}&lt{ls[1:-1]}&gt')
        return f'&lt{fs[1:-1]}&gt{st}&lt{ls[1:-1]}&gt'
    text = re.sub('<(.+)>(.+)</(.+)>', escapeword, string)
    return text
@login_required()
def Home(request):
    story=Story.objects.all()
    # delete expired stories
    for st in story:
        st.expire()
    context = {}
    content_type = {
            'image': [
                'image/png',
                'image/jpg',
                'image/jpeg',
            ],
            'video': [
                'video/mp4'
            ],
            'audio': [
                'audio/mp3'
            ],
            'pdf': [
                'application/pdf'
            ],
            'docx': [
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            ],
            'txt':[
                'text/plain'
            ],
            'web-html':[
                'text/html'
            ]
        }
    
    user = request.user
    # creating new posts
    if request.method == 'POST':
        text = request.POST
        files = request.FILES
        status = text['status']
        estatus = Escape(status)
        medias = files.getlist('medias')
        try:
            error = False
            p = Post.objects.create(author = request.user, status = estatus)
            if files['medias']:
                message = []
                for file in medias:
                    print(file.size)
                    if file.size > 20971520:
                        message.append(f'{file.name} is to large to be saved here!')
                        context['messages'] = message
                        context['status'] = status
                        error = True
                        break
                    else:
                        name = ''
                        if file.content_type in content_type['image']:
                            name = 'image'
                        elif file.content_type in content_type['video']:
                            name = 'video'
                        elif file.content_type in content_type['audio']:
                            name = 'audio'
                        elif file.content_type in content_type['pdf']:
                            name = 'pdf'
                        elif file.content_type in content_type['txt']:
                            name = 'txt'
                        elif file.content_type in content_type['docx']:
                            name = 'docx'
                        elif file.content_type in content_type['web-html']:
                            name = 'html'
                        f = File.objects.create(name = name , file = file)   
                        p.files.add(f)
                if error: 
                    p.delete()
                else: p.save()

        except Exception as e:
            pass
    posts = Post.objects.select_related('author').defer('author__followers','author__followings','author__posts','author__activities').filter(
        Q(author = user) |
        Q(author__username__in = user.followings.values_list('username')) |
        Q(page__name__in = user.pages_followed.values_list('name'))|
        Q(group__name__in = user.groups_in.values_list('name'))
        )
    paginator = Paginator(posts, 15)
    page_number = request.GET.get('page')
    obj_page = paginator.get_page(page_number)
    context['obj_page'] = obj_page
    context['posts'] = posts
    return render(request, 'home/index.html', context)
