from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

def index(request):
    return render(request, 'authentication/index.html')

def register(request):
    form = RegisterForm

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username= username, password=password)
            login(request, user)
            return redirect('index')

        else:
            form = RegisterForm

    content = {'form': form}
    return render(request, 'registration/register.html', content)

def logout(request):
    return render (request, 'registration/logout.html')
