from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


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