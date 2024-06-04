from django.contrib.auth.models import User
from django.db import models
from django.contrib.sessions.models import Session


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} to {self.receiver.username}: {self.content[:20]}'


class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
