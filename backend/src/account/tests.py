from django.test import TestCase  # noqa
import pytest
from django.contrib.auth.models import User
from models import UserSettings, CustomUser

@pytest.mark.django_db
def test_user_settings_creation():
    user = User.objects.create(username="testuser")
    assert UserSettings.objects.filter(user=user).exists()

@pytest.mark.django_db
def test_custom_user_creation():
    user = CustomUser.objects.create(username="customuser")
    assert user.groups.count() == 0
    assert user.user_permissions.count() == 0

@pytest.mark.django_db
def test_user_settings_str_method():
    user = User.objects.create(username="testuser")
    user_settings = UserSettings.objects.create(user=user, display_name="Test User")
    assert str(user_settings) == "Settings for testuser"

