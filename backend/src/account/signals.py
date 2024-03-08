from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import CustomUser, UserSettings


@receiver(post_save, sender=CustomUser)
def create_user_settings(sender, instance, created, **kwargs):
    if created:
        # Create a new UserSettings object for the newly created User
        display_name = instance.last_name + " " + instance.first_name
        if not display_name.strip():
            display_name = instance.username
        UserSettings.objects.create(user=instance, display_name=display_name)
