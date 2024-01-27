from django import forms
from django.contrib.auth.models import User
from usermodelapp.models import userData
from django_recaptcha.fields import ReCaptchaField


class userForm(forms.ModelForm):
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;margin-top:10px', 'class': 'form-control'}),label='')
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px; ', 'class': 'form-control'}),label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px; margin-top:10px', 'class': 'form-control'}),label='')

    class Meta:
        model = User
        fields=['username','email','password']

class userForm2(forms.ModelForm):
    phone=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder' :'Phone', 'style': 'width: 300px;margin-top:10px', 'class': 'form-control'}),label='')
    address=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Address', 'style': 'width: 300px;margin-top:10px', 'class': 'form-control'}),label='')
    class Meta:
        model = userData
        fields = ['phone','address','img']
    captcha = ReCaptchaField(label='')

class userform3(forms.ModelForm):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px; ', 'class': 'form-control'}),label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px; margin-top:10px', 'class': 'form-control'}),label='')

    class Meta:
        model = User
        fields = ['username','email']




