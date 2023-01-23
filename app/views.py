from django.shortcuts import render, redirect
#from .forms import SignUpForm
#from .views import index

"""
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
"""

def index(request):
    #print("Index View Called")
    return render(request, 'index.html')

def login(request):
    #print("Login View Called")
    return render(request, 'login.html')

def signup(request):
    #print("Signup View Called")
    return render(request, 'signup.html')