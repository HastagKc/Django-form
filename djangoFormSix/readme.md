
# Django Student Registration Form Documentation

## Overview

This project demonstrates how to create a student registration form using Django forms, handle form submissions, perform validations, and display validation errors in templates.

## Prerequisites

- Python 3.x
- Django 3.x or later

## Form Definition

The `StudentRegistrationForm` is defined in `forms.py`. This form includes fields for name, age, email, and phone number with appropriate validation and error messages.

### forms.py

```python
from django import forms
from django.core.validators import MinLengthValidator, EmailValidator
from django.core.exceptions import ValidationError

class StudentRegistrationForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
        }),
        validators=[MinLengthValidator(
            2, message='Name must be at least 2 characters long'
        )],
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
            message="Please enter a valid email address"
        )]
    )

    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your phone number'
        }),
        validators=[MinLengthValidator(
            10, message="Phone number must be at least 10 digits long"
        )]
    )

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit():
            raise ValidationError("Phone number must contain only digits")
        return phone
```

## Views Handling Form Submission

The view handles form submission, performs validation, and redirects to a success page if the form is valid.

### views.py

```python
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

def student_view(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            return redirect('success')
    else:
        form = StudentRegistrationForm()

    return render(request, 'base/index.html', {'form': form})

def success(request):
    return render(request, 'base/success.html')
```

## Template to Render the Form and Display Errors

The template renders the form fields and displays validation errors below each field.

### base/index.html

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration</title>
    <link rel="stylesheet" href="{% static 'path/to/bootstrap.css' %}"> <!-- Adjust the path to your Bootstrap CSS -->
</head>

<body>
    <h1>Student Registration</h1>
    <form action="" method="POST" novalidate>
        {% csrf_token %}
        {% for field in form %}
        <div class="form-group">
            {{ field.label_tag }}
            {{ field }}
            {% for error in field.errors %}
            <div class="text-danger">
                {{ error }}
            </div>
            {% endfor %}
        </div>
        {% endfor %}
        <input type="submit" class="btn btn-primary" value="Submit">
    </form>
</body>

</html>
```

### base/success.html

This template is rendered when the form is successfully submitted.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
</head>

<body>
    <h1>Form Submitted Successfully!</h1>
    <p>Your registration was successful.</p>
</body>

</html>
```

## Running the Project

1. **Start the Django server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the form:**
   Navigate to the URL where your form is rendered (e.g., `http://localhost:8000`).

3. **Submit the form:**
   Fill out the form fields and submit it. If there are validation errors, they will be displayed below the respective fields.

4. **Success page:**
   Upon successful submission, you will be redirected to the success page.

## Conclusion

This project demonstrates the basics of creating and handling forms in Django, including field validation, error handling, and user-friendly form rendering using Bootstrap for styling.