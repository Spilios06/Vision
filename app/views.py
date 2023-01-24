from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Get the email and password from the form
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            
            # Check if the passwords match
            if password != password_confirm:
                return render(request, 'signup.html', {'form': form, 'error': 'Passwords do not match'})
            
            # Create a new user
            user = User(email=email, password=password)
            user.save()
            
            # Redirect the user to the homepage
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def index(request):
    #print("Index View Called")
    return render(request, 'index.html')

def login(request):
    #print("Login View Called")
    return render(request, 'login.html')