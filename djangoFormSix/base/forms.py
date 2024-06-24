from django import forms
from django.core.validators import MinLengthValidator, EmailValidator
from django.core.exceptions import ValidationError


class StudentRegistrationFrom(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',

        }),
        validators=[MinLengthValidator(
            2, message='Number must be more than 6 character long')],

    )

    age = forms.IntegerField(
        label='Age',
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your age',

        }),

    )
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }
        ),
        validators=[EmailValidator(
            message="Please Enter valid Email Addrress"
        )
        ]
    )
    phone_number = forms.CharField(
        label='Phone number',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Please enter valid number'
        }),
        validators=[MinLengthValidator(
            10, message="Phone number must be 10 numbers"
        )]
    )

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit():
            raise ValidationError("Phone number must contain only digits")
        return phone
