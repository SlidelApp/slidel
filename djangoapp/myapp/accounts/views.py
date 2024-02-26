from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def create_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Update 'home' with the name of your home page URL
    else:
        form = UserCreationForm()

    return render(request, 'accounts/create_account.html', {'form': form})
