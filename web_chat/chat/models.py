from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=10,unique=True)

class ChatUser(models.Model):
    name = models.CharField(max_length=200)
    login = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Message(models.Model):
    body = models.CharField(max_length=500)
    sender = models.ForeignKey(ChatUser, on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name='receiver')

class Ban(models.Model):
    user = models.OneToOneField(ChatUser)




