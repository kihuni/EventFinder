from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .form import LoginForm

from .models import Event, Attendee, Organizer, Tag, Ticket

# Create your views here.
def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                error_message = 'Invalid username or password.'
    else:
        form = LoginForm()
        error_message = ''
        return render(request, 'login.html', {'form':form,'error_message': error_message})
        
def create_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)   
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'create_account.html', {'form':form})
            
                 