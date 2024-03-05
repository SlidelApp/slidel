from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=60)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", default="default_profile_picture.jpg"
    )

    def __str__(self):
        return f"Settings for {self.user.username}"


@receiver(post_save, sender=User)
def create_user_settings(sender, instance, created, **kwargs):
    if created:
        # Create a new UserSettings object for the newly created User
        display_name = instance.last_name + " " + instance.first_name
        UserSettings.objects.create(user=instance, display_name=display_name)


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
