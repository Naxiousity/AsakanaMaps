from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    """Custom user with email as primary login field."""
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Circle(models.Model):
    name = models.CharField(max_length=100, unique=True)
    invite_code = models.CharField(
        max_length=6,
        unique=True,
        default=lambda: uuid.uuid4().hex[:6]
    )
    members = models.ManyToManyField(
        User,
        through='Membership',
        related_name='circles'
    )


class Membership(models.Model):
    user = models.ForeignKey(Circle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    
