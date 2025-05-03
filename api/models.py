from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import uuid

def generate_invite_code():
    return uuid.uuid4().hex[:6].upper()


class User(AbstractUser):
    """Custom user with email as primary login field."""
    username = models.CharField(max_length=150, unique=False, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Circle(models.Model):
    name = models.CharField(max_length=100, unique=True)
    invite_code = models.CharField(
        max_length=6,
        unique=True,
        default=generate_invite_code,
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='api.Membership',
        through_fields=('circle', 'user'),
        related_name='circles'
    )

class Membership(models.Model):
    """Through model linking Users and Circles."""
    user = models.ForeignKey(
        'api.User',
        on_delete=models.CASCADE,
        related_name='membership_entries'
    )
    circle = models.ForeignKey(
        'api.Circle',
        on_delete=models.CASCADE,
        related_name='membership_entries'
    )
    joined_at = models.DateTimeField(auto_now_add=True)