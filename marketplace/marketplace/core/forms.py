from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 

class LoginForm(AuthenticationForm):
    username =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نام کاربری',
        'class': 'w-full py-4 px-6 rounded-lg'
    }))
    password =  forms.CharField(widget=forms.TextInput(attrs={
         'placeholder': 'رمز عبور',
        'class': 'w-full py-4 px-6 rounded-lg ',
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
        'class': 'w-full py-4 px-6 rounded-lg'
    }))
    first_name =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نام شما',
        'class': 'w-full py-4 px-6 rounded-lg'
    }))
    last_name =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نام خانوادگی شما',
        'class': 'w-full py-4 px-6 rounded-lg'
    }))
    email =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'ایمیل شما',
        'class': 'w-full py-4 px-6 rounded-lg'
    }))
    password1 =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'رمزعبور شما',
        'class': 'w-full py-4 px-6 rounded-lg ',
        'type': 'password' ,
        'name': 'password',
        'autocomplete': 'current-password',
        'id': 'password-field',
    }))
    password2 =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'تکرار رمز عبور',
        'class': 'w-full py-4 px-6 rounded-lg',
        'type': 'password',
        'name':'password',
        'autocomplete': 'current-password',
        'id': 'confirmPassword',
    }))