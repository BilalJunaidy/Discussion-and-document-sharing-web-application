from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
from .models import Profile

#    Don't worry, the UserCreationForm can be easily extended for when I am using a Custom User Model. 
#    Here is the reference for this example:
#    https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
    

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = '__all__'


