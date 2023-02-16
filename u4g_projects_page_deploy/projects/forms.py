from django import forms
from .models import Participant
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    name = forms.CharField(label = "Your name")
    email = forms.EmailField(label = "Your email")
    

class ProjectRequestForm(forms.Form):
    title = forms.CharField(max_length = 200)
    organizer_email = forms.EmailField()
    date = forms.DateField()
    description = forms.CharField(max_length = 1000, widget = forms.Textarea(attrs = {'rows': 20, 'cols': 70}))
    project_image = forms.ImageField()
    location = forms.CharField(max_length = 200)

class CollaborationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = []
        
    members = forms.ModelMultipleChoiceField(
        queryset = Participant.objects.all().order_by("name"),
        widget = forms.CheckboxSelectMultiple
        )

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))
    
    