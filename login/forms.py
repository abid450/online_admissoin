from django import forms
from django.core import validators

class formf(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}))
    email = forms.EmailField(label='Email Address',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),validators=[validators.MinLengthValidator(22)])
    phone = forms.CharField(label='Phone Number',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'+880'}))
    rollnumber = forms.IntegerField(label='Roll Number',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Roll'}))
    regnumber = forms.IntegerField(label='Registration Number',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Registration'}))
    Choise = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
    ]
    Choise = forms.ChoiceField(label='Select Male', choices=Choise ,widget=forms.Select(attrs={'class':'form-control','placeholder':'Select Your Male'}))


    def clean_username(self):
        fulln = self.cleaned_data['username']
        if len(fulln)<4:
            raise forms.ValidationError('Inncorrect name, Please Enter Your Correct Name')
        return fulln
    

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone)<11:
            raise forms.ValidationError('Please Enter Your Phone Number at least (11 Characters of Number)')
        if len(phone)>11:
            raise forms.ValidationError('Please Enter Your Phone Number at least (11 Characters of Number)')
        return phone
    
   