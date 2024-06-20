# Django Form 
---------------

## Introduction
In this documentation we will see a step-by-step guide on creating a Django form that includes radio buttons for selecting gender, rendering the form in a template, handling form submission in a view, and setting up URL routing.

## Step 1: Define the Form Class

First, define a form class using `django.forms.Form` and specify the form fields, including a `ChoiceField` with a `RadioSelect` widget for gender selection.

```python
# forms.py
from django import forms

# Gender choices for the radio buttons
gender = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('None', 'Prefer Not to Say'),
]

# Creating the form class
class StudentRegistration(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    age = forms.IntegerField(label='Your Age')
    
    # Define the ChoiceField with RadioSelect widget
    stu_gender = forms.ChoiceField(
        choices=gender,
        widget=forms.RadioSelect,
        label='Gender',
        required=True
    )
```

## Step 2: Create a View to Handle the Form

Create a view that initializes the form and renders it in a template. For simplicity, this view does not handle form submission, but you can extend it to process submitted data.

```python
# views.py
from django.shortcuts import render
from .forms import StudentRegistration

def studentReg(request):
    # Create an instance of the form
    fm = StudentRegistration()
    return render(request, 'formapp/studentDetails.html', {'form': fm})
```

## Step 3: Create a Template to Render the Form

Create a template to display the form. This template includes the necessary CSRF token for security.

```html
<!-- templates/formapp/studentDetails.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Details</title>
</head>
<body>
    <h2>Student Registration Form</h2>
    <form action="" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

## Step 4: Define URL Patterns

Map a URL to the view you created to render the form.

```python
# urls.py
from django.urls import path
from .views import studentReg

urlpatterns = [
    path("", studentReg, name='studentReg'),
]
```

## Complete File Structure

Your project directory might look like this:

```
myproject/
    myapp/
        __init__.py
        forms.py
        views.py
        urls.py
        templates/
            formapp/
                studentDetails.html
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    manage.py
```

## Additional Steps for Form Handling (Optional)

### Handling Form Submission

To handle form submission, modify the view to process the submitted data:

```python
# views.py
from django.shortcuts import render, redirect
from .forms import StudentRegistration

def studentReg(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            # Process form data here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            stu_gender = form.cleaned_data['stu_gender']
            # You can add logic to save this data to the database, send an email, etc.
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = StudentRegistration()
    return render(request, 'formapp/studentDetails.html', {'form': form})
```

### Update the Template for Error Handling (Optional)

You can update the template to display form errors if the form submission is invalid:

```html
<!-- templates/formapp/studentDetails.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Details</title>
</head>
<body>
    <h2>Student Registration Form</h2>
    <form action="" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        {% if form.errors %}
            <div class="errors">
                <ul>
                    {% for field in form %}
                        {% for error in field.errors %}
                            <li>{{ error }}</li>
                        {% endfor %}
                    {% endfor %}
                </ul>
            </div>
        {% endif %}
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

## Conclusion

This documentation provides a complete guide to creating a Django form with radio buttons, rendering it in a template, handling its submission in a view, and setting up the corresponding URL routing. This basic setup can be extended with additional logic for processing and storing form data, handling form validation errors, and more.

# 2. Manually initialize value, rearranging and manually changing the value of id attribute form view method 

Lets see the below example of Python code with detailed documentation added to explain each part of the `studentReg` function:

```python
from django.shortcuts import render
from .forms import StudentRegistration

def studentReg(request):
    """
    This view handles the registration of a student. It initializes a form
    with default values and customizes various attributes of the form.

    Args:
    - request: HttpRequest object

    Returns:
    - HttpResponse: Rendered HTML page with the form
    """

    # Create an instance of the StudentRegistration form with initial data
    fm = StudentRegistration(
        initial={
            'name': 'Kshittiz Chaudhary',  # Prepopulate the 'name' field
            'age': 25,                     # Prepopulate the 'age' field
            'email': 'chaudharykshittiz950@gmail.com'  # Prepopulate the 'email' field
        }
    )

    # Rearrange the fields of the form. This is useful for customizing the 
    # order in which the fields appear on the template.
    fm.order_fields(field_order=['name', 'age', 'stu_gender', 'email'])

    # Render the template 'studentDetails.html' with the form instance.
    # Pass the form instance to the context dictionary with key 'form'.
    return render(request, 'formapp/studentDetails.html', {'form': fm})
```

### Explanation:

1. **Import Statements**:
    - `from django.shortcuts import render`: Imports the `render` function which is used to generate an HttpResponse that contains the rendered text of a template.
    - `from .forms import StudentRegistration`: Imports the `StudentRegistration` form from the local `forms` module.

2. **Function Definition**:
    - `def studentReg(request)`: Defines the `studentReg` function which takes an `HttpRequest` object as its argument.

3. **Form Initialization**:
    - `fm = StudentRegistration(initial={...})`: Creates an instance of the `StudentRegistration` form, prepopulating it with initial data. The `initial` argument is a dictionary that sets default values for the form fields.

4. **Rearranging Form Fields**:
    - `fm.order_fields(field_order=['name', 'age', 'stu_gender', 'email'])`: Changes the order in which the form fields are displayed. This method takes a list of field names in the desired order.

5. **Rendering the Template**:
    - `return render(request, 'formapp/studentDetails.html', {'form': fm})`: Renders the `studentDetails.html` template, passing the form instance (`fm`) to the template context. The form can then be accessed in the template using the key `'form'`.

This function effectively sets up a student registration form with prepopulated data and customized field ordering, then renders it within the specified HTML template.

# 3. Rendering Forms manually in django Templates / html 

### 1. Using Form Fields Directly

**Description**: Render each form field, its label, and errors directly in the template.

```html
<!-- studentDetails.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student Registration</title>
</head>
<body>
    <h2>Student Registration Form</h2>
    <form method="post">
        {% csrf_token %}
        <div>
            <label for="{{ form.name.id_for_label }}">Name:</label>
            {{ form.name }}
            {{ form.name.errors }}
        </div>
        <div>
            <label for="{{ form.age.id_for_label }}">Age:</label>
            {{ form.age }}
            {{ form.age.errors }}
        </div>
        <div>
            <label for="{{ form.stu_gender.id_for_label }}">Gender:</label>
            {{ form.stu_gender }}
            {{ form.stu_gender.errors }}
        </div>
        <div>
            <label for="{{ form.email.id_for_label }}">Email:</label>
            {{ form.email }}
            {{ form.email.errors }}
        </div>
        <div>
            <button type="submit">Register</button>
        </div>
    </form>
</body>
</html>
```

### 2. Using Form Field Widgets

**Description**: Render the widgets of each form field, which include the input elements.

```html
<!-- studentDetails.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student Registration</title>
</head>
<body>
    <h2>Student Registration Form</h2>
    <form method="post">
        {% csrf_token %}
        <div>
            <label for="{{ form.name.id_for_label }}">Name:</label>
            {{ form.name.widget }}
            {{ form.name.errors }}
        </div>
        <div>
            <label for="{{ form.age.id_for_label }}">Age:</label>
            {{ form.age.widget }}
            {{ form.age.errors }}
        </div>
        <div>
            <label for="{{ form.stu_gender.id_for_label }}">Gender:</label>
            {{ form.stu_gender.widget }}
            {{ form.stu_gender.errors }}
        </div>
        <div>
            <label for="{{ form.email.id_for_label }}">Email:</label>
            {{ form.email.widget }}
            {{ form.email.errors }}
        </div>
        <div>
            <button type="submit">Register</button>
        </div>
    </form>
</body>
</html>
```

### 3. Using a Custom Form Template

**Description**: Create a custom template tag to render each form field, promoting reuse and clean templates.

#### Step 1: Create a Template Tag

```python
# templatetags/form_tags.py
from django import template

register = template.Library()

@register.inclusion_tag('form_field.html')
def render_field(field):
    return {'field': field}
```

#### Step 2: Create the Custom Field Template

```html
<!-- form_field.html -->
<div>
    <label for="{{ field.id_for_label }}">{{ field.label }}:</label>
    {{ field }}
    {% for error in field.errors %}
        <span class="error">{{ error }}</span>
    {% endfor %}
</div>
```

#### Step 3: Use the Custom Tag in Your Form Template

```html
<!-- studentDetails.html -->
{% load form_tags %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student Registration</title>
</head>
<body>
    <h2>Student Registration Form</h2>
    <form method="post">
        {% csrf_token %}
        {% render_field form.name %}
        {% render_field form.age %}
        {% render_field form.stu_gender %}
        {% render_field form.email %}
        <div>
            <button type="submit">Register</button>
        </div>
    </form>
</body>
</html>
```

Each method provides different levels of customization and control over the form's HTML structure and presentation.




