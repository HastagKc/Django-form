### A comprehensive guide covering the full setup for creating and handling a `Student` registration system using Django. This documentation includes the model, form, view, template, and necessary migrations.

---

# Django Student Registration System (Form Api : Model First Approch)

## Overview

This guide outlines the steps to create a simple Student Registration System using Django. The system includes:

- A Django model for storing student data.
- A form for user input.
- A view to handle form submission.
- Templates for displaying the form and success messages.

## 1. **Model Definition**

**`models.py`**

The `Student` model is designed to store the following information:

- Name
- Age
- Email
- Phone Number

### Code

```python
from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

class Student(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2, message='Name must be more than 2 characters long')
        ]
    )
    age = models.PositiveIntegerField()
    email = models.EmailField(
        validators=[
            EmailValidator(message="Please enter a valid email address")
        ]
    )
    phone_number = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(10, message="Phone number must be 10 digits long")
        ]
    )

    def __str__(self):
        return self.name
```

### Explanation

- **`name`**: A `CharField` with a maximum length of 100 characters and a minimum length validator.
- **`age`**: A positive integer field.
- **`email`**: An `EmailField` with an email validator.
- **`phone_number`**: A `CharField` with a maximum length of 10 characters and a minimum length validator.

### Migrations

To apply the model changes to the database:

1. **Create Migration Files**:

   ```bash
   python manage.py makemigrations
   ```

2. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

## 2. **Form Definition**

**`forms.py`**

The `StudentRegistrationForm` is a `ModelForm` that generates a form based on the `Student` model.

### Code

```python
from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your age'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits")
        return phone
```

### Explanation

- **Meta Class**: Specifies the model and fields to be included in the form. Customizes widgets for form fields.
- **`clean_phone_number` Method**: Adds additional validation to ensure the phone number contains only digits.

## 3. **View Definition**

**`views.py`**

The view handles form rendering and processing.

### Code

```python
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})
```

### Explanation

- **POST Request**: Processes the form data and saves it to the database if the form is valid.
- **GET Request**: Displays the empty form for user input.

## 4. **Template Definitions**

### **`register.html`**

The form template for rendering the registration form.

### Code

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Student Registration</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRz4G1gf6lZ5QVUVGg9LN7L9/qe2to0/tQcmU8d2"
      crossorigin="anonymous"
    />
  </head>

  <body class="bg-light">
    <div class="container mt-5">
      <h1 class="mb-4">Student Registration</h1>
      <form
        action=""
        method="POST"
        novalidate
        class="bg-white p-4 rounded shadow-sm"
      >
        {% csrf_token %}

        <!-- Display form errors -->
        {% if form.non_field_errors %}
        <div class="alert alert-danger">
          {% for error in form.non_field_errors %}
          <p>{{ error }}</p>
          {% endfor %}
        </div>
        {% endif %}

        <!-- Iterate through form fields -->
        {% for field in form %}
        <div class="mb-3">
          {{ field.label_tag(attrs={'class': 'form-label'}) }} {{
          field|add_class:"form-control" }} {% if field.errors %}
          <div class="text-danger mt-1">
            {% for error in field.errors %}
            <p>{{ error }}</p>
            {% endfor %}
          </div>
          {% endif %}
        </div>
        {% endfor %}

        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-4MtfOHmOlDMLK00fQRyVYRAzX+y+mFA6JkOqQ5l5q5Io1pcfFxfrocf2KNW4Q4c7"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

### Explanation

- **Bootstrap Integration**: For styling and responsive design.
- **Form Rendering**: Displays the form and handles field errors.
- **Error Display**: Shows form and field-specific errors.

### **`success.html`**

A simple success page displayed after form submission.

### Code

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Registration Successful</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
  </head>

  <body class="bg-light">
    <div class="container mt-5">
      <h1 class="text-success">Registration Successful</h1>
      <p>Your registration has been successfully submitted.</p>
    </div>
  </body>
</html>
```

### Explanation

- **Simple Success Message**: Displays a message confirming successful registration.

## 5. **URL Configuration**

Add URL patterns to connect the view to a URL endpoint.

**`urls.py`**

### Code

```python
from django.urls import path
from .views import register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
]
```

### Explanation

- **`register/`**: URL for the registration form.
- **`success/`**: URL for the success page.

## Conclusion

This setup provides a complete registration system with user-friendly form handling, validation, and data storage. You can further customize the templates, add more fields or validation logic, and enhance the functionality as needed.

Feel free to ask if you have any questions or need further customization!
