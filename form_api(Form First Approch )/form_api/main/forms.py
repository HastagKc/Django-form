from django import forms
from django.core.validators import MinLengthValidator, EmailValidator


class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label='name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }
        ),
    )
    age = forms.IntegerField(
        min_value=0,
        label='Age',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your age',
            }
        ),
    )
