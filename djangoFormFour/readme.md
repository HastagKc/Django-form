# Feteching Data in terminal from Form in django

In this README documentation for your Django project with the `StudentRegistration` form and `showstudentdata` view:

## Project Setup

### Prerequisites
- Python 3.x
- Django 3.x or higher

### Installation

1. **Create and activate a virtual environment**:
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

2. **Install Django**:
    ```sh
    pip install django
    ```

3. **Create a new Django project**:
    ```sh
    django-admin startproject myproject
    cd myproject
    ```

4. **Create a new Django app**:
    ```sh
    python manage.py startapp main
    ```

### Configuration

1. **Add the app to `INSTALLED_APPS`** in `myproject/settings.py`:
    ```python
    INSTALLED_APPS = [
        ...
        'main',
    ]
    ```

2. **Create the form** in `main/forms.py`:
    ```python
    from django import forms

    class StudentRegistration(forms.Form):
        name = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'name', 'placeholder': 'Enter your name'}
        ))
        email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
            'class': 'email',
            'placeholder': 'Enter your email',
        }))
    ```

3. **Create the view** in `main/views.py`:
    ```python
    from django.shortcuts import render
    from .forms import StudentRegistration

    # Create your views here.
    def showstudentdata(request):
        if request.method == "POST":
            # create object of form class
            fm = StudentRegistration(request.POST)
            if fm.is_valid():
                print("Form is valid ")
                print(f'name: {fm.cleaned_data["name"]}')
                print(f'email: {fm.cleaned_data["email"]}')
        else:
            fm = StudentRegistration()

        return render(request, 'main/studentform.html', {'form': fm})
    ```

4. **Create the template** in `main/templates/main/studentform.html`:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student Registration</title>
    </head>
    <body>
        <form action="" method="POST">
            {% csrf_token %}
            {{ form }}
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    ```

5. **Configure URL routing** in `myproject/urls.py`:
    ```python
    from django.contrib import admin
    from django.urls import path
    from main import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('student/', views.showstudentdata, name='showstudentdata'),
    ]
    ```

### Running the Project

1. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

2. **Run the server**:
    ```sh
    python manage.py runserver
    ```

3. **Access the form**:
    Open your web browser and navigate to `http://127.0.0.1:8000/student/` to see the student registration form.

### Summary

- **Form**: The `StudentRegistration` form contains `name` and `email` fields with basic validation and HTML attributes for styling.
- **View**: The `showstudentdata` view handles the form submission, validates the data, and prints the cleaned data to the console.
- **Template**: The `studentform.html` template renders the form with CSRF protection and a submit button.

### Notes

- Ensure that you have set up CSRF protection correctly in your Django settings and templates.
- This is a simple example to get you started with forms and views in Django. For more advanced features, refer to the [official Django documentation](https://docs.djangoproject.com/).

This README should help you set up and run your Django project with the `StudentRegistration` form and view.