from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, FormView
from .models import User
from .forms import RegisterForm, LoginForm

class UserCreateView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

class UserLoginView(FormView):
    model = User
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('index')

# Create your views here.
def index(request):
  return render(request, 'index.html')

def login(request):
  return render(request, 'registration/login.html')

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

