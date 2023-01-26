from django import forms

class UserCreationForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=255)
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm Password', max_length=255, widget=forms.PasswordInput)