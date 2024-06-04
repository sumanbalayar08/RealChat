import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from django.contrib.auth.models import User
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the user and room information from the scope
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['username']
        self.room_group_name = f'chat_{self.room_name}'

        # Add the user to the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from the room group upon disconnection
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive message data from WebSocket
        data = json.loads(text_data)
        message = data['message']
        receiver_username = data['receiver']

        # Get the receiver user object
        receiver = await database_sync_to_async(User.objects.get)(username=receiver_username)

        # Save the message to the database
        saved_message = await database_sync_to_async(Message.objects.create)(
            sender=self.user, receiver=receiver, content=message
        )

        # Send the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.user.username,
                'time': saved_message.timestamp.strftime('%H:%M')
            }
        )

    async def chat_message(self, event):
        # Receive message from room group
        message = event['message']
        sender = event['sender']
        time = event['time']

        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'time': time
        }))

    async def user_logout(self, event):
        # Receive logout event
        user_id = event['user_id']
        username = event['username']

        # Send logout notification to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'user_logout',
            'user_id': user_id,
            'username': username,
        }))
