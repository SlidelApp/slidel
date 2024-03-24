from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserSettings

class SettingsEndpoint(APIView):

    def get(self, request):
        settings = UserSettings.objects.get(user=request.user)
        return Response(
            {
                "display_name": settings.display_name,
                "profile_picture": settings.profile_picture.url,
            }
        )
    
    def post(self, request):
        settings = UserSettings.objects.get(user=request.user)
        settings.display_name = request.data["display_name"]
        settings.save()
        return Response(
            {
                "display_name": settings.display_name,
                "profile_picture": settings.profile_picture.url,
            }
        )


def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

        return render(request, "create_account.html", {"form": form})


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class YourApiView(APIView):
    def get(self, request):
        # view logic here...
        return Response({"message": "Authenticated successfully!"})
