from django.db.models.query import Q
from django.shortcuts import redirect, render
from django.http import HttpResponse
import json
from home.views import Post, PostNotification, User
from .ruleValidators import Check
from .models import Group
from notifications.notifcations import GroupPostNotification

from activities.models import Activity
# Create your views here.

def GroupView(request, gid):
    group = Group.objects.get(id=gid)
    context = {}
    context['group'] = group
    a = Activity.objects.create(activity = f'{group.name}', description=f'You visit to check')
    request.user.activities.add(a)
    private = group.private
    if request.user in group.members.all():
        userIn = True
    else:
        userIn = False
    context['userIn'] = userIn
    context['private'] = private
    print(group.group_post.all())
    return render(request, 'groups/group.html', context)
def Groups(request):
    if request.method == 'POST':
        user = request.user
        group_name = request.POST['group-name']
        try:
            group_name = group_name.replace(' ','_')
            group = Group.objects.create(creator = user, name = group_name)
            group.members.add(user)
            return redirect('group:group', group.id)
        except Exception as e:
            print(e)

    groups = Group.objects.exclude(creator = request.user)
    mgroups = Group.objects.filter(creator = request.user)
    context = {}
    context['groups'] = groups
    context['mgroups'] = mgroups
    return render(request, 'groups/groups.html', context)
def GroupPost(request, gid):
    json_dumbs = json.loads(request.body)
    text = json_dumbs['text']
    username = json_dumbs['username']
    user = User.objects.get(username = username)
    group = Group.objects.get(id=gid)
    rules = group.rules.all()
    if Check(text, rules):
        # do some magic
        p = Post.objects.create(status = text, author = user)
        group.w_posts.add(p)
        GroupPostNotification('post_not_allowed', user, group.admins.all(), p , group ,True).send()
        return HttpResponse('not allowed')
    else:
        try:
            p = Post.objects.create(status = text, author = user)
            p.group = group
            p.save()
            PostNotification('post', user, group.members.all(), True).send()
        except Exception as e:
            print(e)
            pass
    a = Activity.objects.create(activity = f'{group.name}', description=f'You posted')
    request.user.activities.add(a)

    return HttpResponse('thanks')
def GroupSetting(request, gid):

    if request.method == 'POST':
        pass
    context = {}
    group = Group.objects.get(id = gid)
    context['group'] = group
    return render(request,'groups/group.setting.html', context)
def GroupJoinLeave(request, gid):
    group = Group.objects.get(id = gid)
    user = request.user
    if user in group.members.all():
        group.members.remove(user)
        return redirect('group:groups')
    else:
        group.members.add(user)
        return redirect('group:group', gid)
def GroupPrivacy(request, gid):
    group = Group.objects.get(id = gid)
    if group.private:
        group.private = False
    else:
        group.private = True
    group.save()
    return redirect('group:group', gid)
def GroupMembers(request, gid):
    context = {}
    group = Group.objects.get(id = gid)
    context['members'] = group.members.all()
    context['creator'] = group.creator
    context['groupId'] = group.id
    context['admins'] = group.admins.all()
    return render(request, 'groups/group.members.html', context)
def GroupMakeAdmin(request, gid, uid):
    user = User.objects.get(id = uid)
    group = Group.objects.get(id = gid)
    if user in group.admins.all():
        group.admins.remove(user)
    else:
        group.admins.add(user)
    return redirect('group:group-members', gid)