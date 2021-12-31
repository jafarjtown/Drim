
from groups.models import Group
from django.http.response import HttpResponse
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from .models import Post, Story
from accounts.models import User
from itertools import chain
from django.http import JsonResponse
from Files.models import File
from pages.models import Page
from institution.models import Institution
class UserSerializerPost(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'avatar', 'is_student', 'is_teacher']
class GroupSetSerializerPost(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'private','id']

class instSetSerializerPost(ModelSerializer):
    class Meta:
        model = Institution
        fields = ['name','logo', 'id','verified']

class pageSetSerializerPost(ModelSerializer):
    class Meta:
        model = Page
        fields = ['name', 'verified']

class PostSerializer(ModelSerializer):
    author = UserSerializerPost()
    group = GroupSetSerializerPost(many=True)
    page = pageSetSerializerPost(many=True)
    institution = instSetSerializerPost(many=True)
    
    class Meta:
        model = Post
        fields = '__all__'
        depth = 3
        


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related('likes','comments').select_related('author').order_by('-created_at')
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        users = [user for user in user.followings.all()]
        userGroups = [group for group in user.groups_in.all()]
        posts = []
        qs = None
        for u in users:
            u_post = Post.objects.filter(author = u)
            posts.append(u_post)
        for gp in userGroups:
            gp_post = Post.objects.filter(group = gp)
            posts.append(gp_post)
        my_posts = Post.objects.filter(author = user)
        posts.append(my_posts)
        if posts and len(posts)>0:
            qs = sorted(chain(*posts), reverse=True, key=lambda obj : obj.created_at)
        else:
            return JsonResponse({
                'error':'error'
            })
        return list(set(qs))
    
    def create(self, request, *args, **kwargs):
        user = request.user
        status = request.POST['status']
        # self.author = request.user
        p = Post.objects.create(author = user, status = status)

        if request.FILES['files']:
            for file in request.FILES.getlist('files'):
                f = File.objects.create(name = 'status' , file= file)
            p.files.add(f)
        return HttpResponse('done')


class StorySerializer(ModelSerializer):
    user = UserSerializerPost()

    class Meta:
        model = Story
        fields = '__all__'
        depth = 2


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def get_queryset(self):
        user = self.request.user
        users = [user for user in user.followings.all()]
        stories = []
        qs = None
        for u in users:
            u_story = Story.objects.filter(user=u)
            stories.append(u_story)
        my_stories = Story.objects.filter(user=user)
        stories.append(my_stories)
        if stories and len(stories) > 0:
            qs = sorted(chain(*stories), reverse=True, key=lambda obj: obj.upload_on)
        else:
            return JsonResponse({
                'error': 'error'
            })
        return list(set(qs))

    def create(self, request, *args, **kwargs):
        user = request.user
        status = request.POST['status']
        file = request.FILES['file']
        Story.objects.create(user=user, caption=status, file=file)
        return HttpResponse('done')


class PostViewSetDetail(viewsets.ModelViewSet):
    queryset = Post.objects.prefetch_related('likes','comments').select_related('author').order_by('-created_at')
    serializer_class = PostSerializer

