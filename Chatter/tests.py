from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Message
from asgiref.sync import sync_to_async
from django.test import TransactionTestCase
from channels.testing import WebsocketCommunicator
from RealChat.asgi import application


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')

    def test_signup_view(self):
        response = self.client.post(reverse('signup'), {
        'username': 'newuser', 'email': 'newuser@example.com', 'password1': '12345', 'password2': '12345'})
        # Check if the user is redirected after signup
        self.assertEqual(response.status_code, 302)

    def test_login_view(self):
        response = self.client.post(
            reverse('login'), {'username': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('logout'))
        # Check if the user is redirected after logout
        self.assertEqual(response.status_code, 302)


class WebSocketTestCase(TransactionTestCase):
    def setUp(self):
        # Create users synchronously
        self.user1 = User.objects.create_user(
            username='user1', password='12345')
        self.user2 = User.objects.create_user(
            username='user2', password='12345')

    async def test_chat_consumer(self):
        # Authenticate user1 and create a communicator for user1
        communicator = WebsocketCommunicator(
            application, f'/ws/chat/{self.user2.username}/')
        communicator.scope['user'] = self.user1
        communicator.scope['url_route'] = {
            'kwargs': {'username': self.user2.username}}

        # Connect to WebSocket
        connected, subprotocol = await communicator.connect()
        assert connected

        # Send a message from user1 to user2
        message_data = {
            'message': 'Hello, user2!',
            'receiver': self.user2.username,
        }
        await communicator.send_json_to(message_data)

        # Check if the message was broadcasted to the room group
        response = await communicator.receive_json_from()
        assert response['message'] == 'Hello, user2!'
        assert response['sender'] == self.user1.username

        # Check if the message is saved in the database
        message = await sync_to_async(Message.objects.get)(
            sender=self.user1, receiver=self.user2, content='Hello, user2!'
        )
        assert message is not None

        # Disconnect the WebSocket
        await communicator.disconnect()
