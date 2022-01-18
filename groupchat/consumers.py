from accounts.models import User
import json
from message.models import ChatBox, Message, Thread
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async

class GroupChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.me = self.scope['user']
        self.room_group_name = f'chat_{self.room_name}'
        

        # Join romm
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': f'{self.me.username} join the Group',
                'user': self.me.username,
                'join': True,
                'offline': False
            }
        )
        await self.accept()
        # return super().connect()
    async def disconnect(self, code):
        # Leave room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': f'{self.me.username} left the Group',
                'user': self.me.username,
                'offline': True,
                'join': False

            }
        )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        pass
        # return super().disconnect(code)
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

       # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.me.username,
                'offline': False,
                'join': False
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        left = event['offline']
        join = event['join']
    

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'offline': left,
            'join': join
        }))

class OneToOneChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.thread_id = self.scope['url_route']['kwargs']['thread_id']
        self.me = self.scope['user']
        self.thread_group_name = f'personal_chat_{self.thread_id}'
        

        # Join romm
        await self.channel_layer.group_add(
            self.thread_group_name,
            self.channel_name
        )
        # await self.channel_layer.group_send(
        #     self.thread_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': f'{self.me.username} join the Group',
        #         'user': self.me.username,
        #         'join': True,
        #         'offline': False
        #     }
        # )
        await self.accept()
        # return super().connect()
    async def disconnect(self, code):
        # Leave room group
        # await self.channel_layer.group_send(
        #     self.thread_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': f'{self.me.username} left the Group',
        #         'user': self.me.username,
        #         'offline': True,
        #         'join': False

        #     }
        # )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        pass
        # return super().disconnect(code)
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.save_messages(message)
       # Send message to room group
        await self.channel_layer.group_send(
            self.thread_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.me.username,
                'offline': False,
                'join': False
            }
        )
    @database_sync_to_async
    def save_messages(self, text):
        thread = Thread.objects.get(id = self.thread_id).chats
        friendchat = thread.exclude(friend__resipient = self.me)
        id = friendchat[0].friend.resipient.id
        friend = User.objects.prefetch_related('followers','followings','activities').get(id = id)
        user = User.objects.prefetch_related('followers','followings','activities').get(username = self.me.username)
        userchat = user.user_chat.chats.get( friend__resipient = friend)
        userchat.seen()
        friendchat = friend.user_chat.chats
        chatbox = friendchat.get(friend__resipient = user)
        m = Message.objects.create(sender = user, receiver = friend, text = text)
        userchat.messages.add(m)
        chatbox.messages.add(m)
        chatbox.unseen_messages.add(m)
        userchat.save()

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        left = event['offline']
        join = event['join']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'offline': left,
            'join': join
        }))