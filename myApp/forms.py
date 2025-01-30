from .models import User, Blog
from django import forms
from django.contrib.auth.hashers import make_password


class RegisterForm(forms.ModelForm):
  confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput())

  class Meta:
    model = User
    fields = ['email', 'password']
    widget = {
      "password" : forms.PasswordInput()
    }

  def save(self, commit=True):
        user = super().save(commit=False) # create but not save the data
        user.password = make_password(self.cleaned_data['password']) # make_password hashes the password
        if commit:
            user.save() # optionally save to database
        return user

class LoginForm(forms.Form):
  email = forms.EmailField(max_length=200)
  password = forms.CharField(max_length=100, widget=forms.PasswordInput())