from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text', )
        
        
        
class JoinForm(UserCreationForm):
    
    '''class Meta:
        model = User
        fields = ('username', 'password', 'email', )'''
        
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(max_length = 254, widget = forms.TextInput())
    password = forms.CharField(max_length = 254, widget = forms.PasswordInput())