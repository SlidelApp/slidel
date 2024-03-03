from multiprocessing import AuthenticationError
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView



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


@authentication_classes([AuthenticationError])
@permission_classes([IsAuthenticated])
class YourApiView(APIView):
    def get(self, request):
        return Response({"message": "Authenticated successfully!"})
    
    def get(self, request):
        # View logic
        user = request.user  # The authenticated user
        response_data = {
            'message': 'Authenticated successfully!',
            'user_id': user.id,
            'username': user.username,
        }
        return Response(response_data)