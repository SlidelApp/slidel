from django.urls import path

from .views import create_account

urlpatterns = [
    path("create/", create_account, name="create_account"),
]
