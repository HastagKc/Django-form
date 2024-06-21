### In this repo will see the Form Field argument


# Django Form with Custom Error Messages and FormField

## Overview

This documentation provides a step-by-step guide to creating a Django form with custom error messages for each field. It covers defining the form, adding custom error messages, and rendering the form with error messages in a template.

## 1. Defining the Form with Custom Error Messages

Create a form with custom error messages for each field.

```python
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
```

## 2. Using the Form in a View

Create a view to handle the form submission and display any validation errors.

```python
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subscribe = form.cleaned_data['subscribe']
            preferred_contact_time = form.cleaned_data['preferred_contact_time']
            birthday = form.cleaned_data['birthday']
            # Save or send the data
            return render(request, 'contact_success.html', {'name': name})
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})
```

## 3. Rendering the Form in a Template

Create a template to display the form along with the error messages.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact Form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h2>Contact Us</h2>
        <form method="post" novalidate>
            {% csrf_token %}
            <div class="form-group">
                {{ form.name.label_tag }}
                {{ form.name }}
                {% if form.name.errors %}
                    <div class="alert alert-danger">{{ form.name.errors }}</div>
                {% endif %}
                <small class="form-text text-muted">{{ form.name.help_text }}</small>
            </div>
            <div class="form-group">
                {{ form.email.label_tag }}
                {{ form.email }}
                {% if form.email.errors %}
                    <div class="alert alert-danger">{{ form.email.errors }}</div>
                {% endif %}
            </div>
            <div class="form-group">
                {{ form.message.label_tag }}
                {{ form.message }}
                {% if form.message.errors %}
                    <div class="alert alert-danger">{{ form.message.errors }}</div>
                {% endif %}
            </div>
            <div class="form-group form-check">
                {{ form.subscribe }}
                {{ form.subscribe.label_tag }}
            </div>
            <div class="form-group">
                {{ form.preferred_contact_time.label_tag }}
                {{ form.preferred_contact_time }}
                {% if form.preferred_contact_time.errors %}
                    <div class="alert alert-danger">{{ form.preferred_contact_time.errors }}</div>
                {% endif %}
            </div>
            <div class="form-group">
                {{ form.birthday.label_tag }}
                {{ form.birthday }}
                {% if form.birthday.errors %}
                    <div class="alert alert-danger">{{ form.birthday.errors }}</div>
                {% endif %}
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>
```

## Summary

This documentation provides a step-by-step guide to creating a Django form with custom error messages for each field:

1. **Form Definition**: Create a form class with custom error messages using the `error_messages` argument in each field.
2. **View Handling**: Define a view to handle form submissions and display validation errors.
3. **Template Rendering**: Create a template to render the form and show error messages using Bootstrap for styling.

With this setup, users will see customized error messages next to each field when they submit invalid data, enhancing the user experience by providing clear and specific feedback.