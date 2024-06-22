from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'name', 'placeholder': 'Enter your name'}
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'email',
        'placeholder': 'Enter your email',
    }))
