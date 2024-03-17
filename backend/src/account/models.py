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

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    users = models.ManyToManyField(
        CustomUser,
        verbose_name="subscribed users",
        blank=True,
        related_name="subscriptions",
        related_query_name="subscription",
    )

    def __str__(self):
        return self.name


class UserSettings(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=60)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", default="default_profile_picture.jpg"
    )

    def __str__(self):
        return f"Settings for {self.user.username}"
