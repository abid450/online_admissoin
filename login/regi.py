from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class register_f(UserCreationForm):
    profe_choice = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Doctor', 'Doctor'),
        ('Engineer', 'Engineer'),

    ]
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}))
    email = forms.EmailField(label='Email Address',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Your Password'}))
    profession = forms.ChoiceField(label='Choice Your Profession', choices=profe_choice, widget=forms.Select(attrs={'class':'form-control','placeholder':'Choice Profession'}))


    class Meta:
        model = User
        fields = ['username','email','password1','password2','profession']


# Change User -----------------------------------------------------------
class change_u(UserChangeForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your User'}))
    email = forms.EmailField(label='Email Address',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    date_joined = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Date Joined'}))
    last_login = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Last Login'}))
    
    password = None
    class Meta:
        model = User
        fields = ['username','email','date_joined','last_login']


# Userprofile -------------------------------------
class UserProfileForm(forms.ModelForm):
    
    
    class Meta:
        model=UserProfile
        fields = ['title','Birth_Date','Blood_Group']
        

