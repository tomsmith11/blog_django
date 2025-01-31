from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  return render(request, 'index.html')
  
def register_view(request):  # Separate registration view
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            return HttpResponse('Email already exists')

        # Create user using Django's User model
        user = User.objects.create_user(
            username=email,  # Using email as username
            email=email,
            password=password,  # This will hash the password automatically
            first_name=first_name,
            last_name=last_name
        )

        
        return redirect('login')
    return render(request, 'ecommerce/form/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate using username (email in this case)
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            return HttpResponse('Invalid credentials')
            
    return render(request, 'ecommerce/form/login.html')

@login_required
def create_blog(request):
  if request.method == "POST":
    title = request.POST.get("title")
    content = request.POST.get("content")
    Blog.objects.create(
      title=title,
      content=content,
      author=request.user
    )
    return redirect('index')
  
  return render(request, 'create_blog.html')


def logout_view(request):
    logout(request)
    return redirect('login')
