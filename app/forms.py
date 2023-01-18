from django import forms
from .models import User
from .forms import SignUpForm

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')