# Form Api (Form First approch)

### 1. Create the Form

First, we define the form in `forms.py`.

**forms.py:**

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
            6, message='Name must be more than 6 characters long'
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
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
        }),
        validators=[EmailValidator(
            message="Please enter a valid email address"
        )],
    )

    phone_number = forms.CharField(
        label='Phone number',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your phone number'
        }),
        validators=[MinLengthValidator(
            10, message="Phone number must be 10 digits long"
        )],
    )

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit():
            raise ValidationError("Phone number must contain only digits")
        return phone
```

### 2. Create the Model

Next, we create the corresponding model in `models.py`.

**models.py:**

```python
from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

class Student(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(6, message='Name must be more than 6 characters long')
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

### 3. Create and Apply Migrations

After defining the model, create and apply migrations to update the database schema.

1. **Create the migration file:**

```bash
python manage.py makemigrations
```

2. **Apply the migration:**

```bash
python manage.py migrate
```

### 4. Update the View to Handle Form Submission

Update your view to handle form submission and save the data to the database.

**views.py:**

```python
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .models import Student

def register_view(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            Student.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number']
            )
            return redirect('success')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})
```

### 5. Update URL Configuration

Add the view to your URL configuration.

**urls.py:**

```python
from django.urls import path
from .views import register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
]
```

### 6. Create register template

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

### 7. Create the Success Template

Create a simple template to display upon successful registration.

**templates/success.html:**

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

With these steps, you have a fully functional student registration form that stores data in the database using a Django model.

# Why validations apply both in form as well as in model ?

Validators in Django can be applied at both the form and model levels. Each serves a specific purpose, and having them in both places is generally for different types of validation scenarios. Here’s a breakdown of why you might include validators in both forms and models:

### 1. **Model Validators**

**Purpose:**

- **Database Integrity:** Validators on the model level ensure that data stored in the database adheres to certain rules. These validators are enforced whenever data is saved or updated in the database.
- **Reusability:** Validators on models are useful when you want to ensure data integrity across different parts of your application, such as through Django’s admin interface, custom scripts, or any other method of data entry.
- **Consistency:** They provide a single point of truth for data validation that is enforced regardless of how or where the data is entered.

**Example in Model:**

```python
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
```

### 2. **Form Validators**

**Purpose:**

- **User Input Validation:** Validators on the form level ensure that the data entered by users through web forms is valid before being processed or saved. They provide immediate feedback to users about the correctness of their input.
- **User Experience:** Form validators are helpful for providing real-time validation feedback in the UI, guiding users to correct errors before submitting the form.
- **Custom Logic:** Form validators can include custom validation logic that’s specific to the form’s use case and might not be suitable for all cases where the model is used.

**Example in Form:**

```python
class StudentRegistrationForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
        }),
        validators=[MinLengthValidator(
            2, message='Name must be more than 2 characters long'
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
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
        }),
        validators=[EmailValidator(
            message="Please enter a valid email address"
        )],
    )

    phone_number = forms.CharField(
        label='Phone number',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your phone number'
        }),
        validators=[MinLengthValidator(
            10, message="Phone number must be 10 digits long"
        )],
    )

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit():
            raise ValidationError("Phone number must contain only digits")
        return phone
```

### **When to Use Validators in Both**

- **Redundancy for Safety:** Using validators in both forms and models can act as a safeguard. For instance, even if the form validation fails (e.g., due to user input errors), the model validation ensures that invalid data cannot be saved directly to the database.
- **Different Contexts:** Form validators handle user input and feedback, while model validators handle data consistency in the database.

### **In Summary**

- **Model Validators**: Ensure data integrity in the database and enforce rules across various data entry methods.
- **Form Validators**: Provide user feedback and ensure that data submitted through web forms is valid before processing or saving it.

Having validators at both levels ensures robust validation handling and improves the overall reliability of your application.
