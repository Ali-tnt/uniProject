from django import forms
from django.contrib.auth import user_logged_out
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 

INPUT_CLASSES  = 'w-full py-4 px-6 rounded-lg'

class LoginForm(AuthenticationForm):
    username =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نام کاربری',
        'class': INPUT_CLASSES
    }))
    password =  forms.CharField(widget=forms.TextInput(attrs={
         'placeholder': 'رمز عبور',
        'class': INPUT_CLASSES,
        'type': 'password' ,
        'name': 'password',
        'autocomplete': 'current-password',
        'id': 'password-field',
    }))

class SignupForm(UserCreationForm):
    class Meta: 
        model = User 
        fields = ('first_name','last_name', 'username', 'email', 'password1', 'password2', ) 
    username =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نام کاربری موردنظر',
        'class': INPUT_CLASSES
    }))
    first_name =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نام شما',
        'class': INPUT_CLASSES
    }))
    last_name =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نام خانوادگی شما',
        'class': INPUT_CLASSES
    }))
    email =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'ایمیل شما',
        'class': INPUT_CLASSES
    }))
    password1 =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'رمزعبور شما',
        'class': INPUT_CLASSES,
        'type': 'password' ,
        'name': 'password',
        'autocomplete': 'current-password',
        'id': 'password-field',
    }))
    password2 =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'تکرار رمز عبور',
        'class': INPUT_CLASSES,
        'type': 'password',
        'name':'password',
        'autocomplete': 'current-password',
        'id': 'confirmPassword',
    }))