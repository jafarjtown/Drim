from .models import Notification

class PostNotification:
    def __init__(self, _type, _from, _to, _many = False):
        self._from = _from
        self._to = _to
        self._many = _many
        self._type = _type
    
    def send(self):
        if self._many:
            for user in self._to:
                if self._type == 'comment':
                    message = f'Dear {user.username}, {self._from.username} just commented on the post you are following..'
                elif self._type == 'post':
                    message = f'Dear {user.username}, {self._from.username} just posted an update'
                Notification.objects.create(_from=self._from, _to=user, message=message)
                pass
            pass
        else:
            if self._type == 'comment':
                message = f'Dear {self._to.username}, {self._from.username} just commented on your post'
                Notification.objects.create(_from=self._from, _to=self._to, message=message)
            pass

class FriendRequestNotification:
    def __init__(self, _to, _from, _type):
        self._to = _to
        self._from = _from
        self._type = _type

    def send(self):
        if self._type == 'follow':
            message = f'dear {self._to.first_name} {self._to.last_name}, {self._from.first_name} {self._from.last_name} followed you'
        elif self._type == 'unfollow':
            message = f'dear {self._to.username}, {self._from.username} just accept your friend request'
        Notification.objects.create(_from=self._from, _to=self._to, message=message)

class GroupPostNotification:
    def __init__(self, _type, _from, _to, _post , _group,_many = False,):
        self._from = _from
        self._to = _to
        self._many = _many
        self._type = _type
        self._post = _post
        self._group = _group

    def send(self):
        if self._many:
            print(self._to)
            for user in self._to:
                if self._type == 'post':
                    message = f'Dear {user.username}, {self._from.username} just create a new post.. \n click <a href="#">view</a> to check'
                elif self._type == 'post_not_allowed':
                    message = f'Dear {user.username}, {self._from.username} just go against the rule in {self._group.name} \n click <a href="/posts/comments/{self._post.id}/">view</a> to check'
                Notification.objects.create(_from=self._from, _to=user, message=message)
                pass
            pass
        else:
            if self._type == 'post':
                message = f'Dear {self._to.username}, {self._from.username} just go against the rule'
                Notification.objects.create(_from=self._from, _to=self._to, message=message)
            pass
