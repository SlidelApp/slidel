from django.db import models  # noqa
from django.contrib.auth.models import User
from django.db import models

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=150)  # Assuming the same max length as User.username
    password = models.CharField(max_length=128)  # Assuming the same max length as User.password
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)  # Example using ImageField

    def __str__(self):
        return f"Settings for {self.user.username}"


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        related_name="customuser_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        related_name="customuser_set",
        related_query_name="user",
    )
