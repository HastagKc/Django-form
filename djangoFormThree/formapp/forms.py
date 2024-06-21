from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter your full name",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Full Name'
        }),
        error_messages={
            'required': 'Name is required.',
            'max_length': 'Name cannot exceed 100 characters.'
        }
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address'
        }),
        error_messages={
            'required': 'Email is required.',
            'invalid': 'Enter a valid email address.'
        }
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Your message',
            'rows': 5
        }),
        error_messages={
            'required': 'Message is required.'
        }
    )
    subscribe = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    preferred_contact_time = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'HH:MM'
        }),
        error_messages={
            'invalid': 'Enter a valid time in HH:MM format.'
        }
    )
    birthday = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD'
        }),
        error_messages={
            'invalid': 'Enter a valid date in YYYY-MM-DD format.'
        }
    )
