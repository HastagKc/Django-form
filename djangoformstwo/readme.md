## In this project we will see how to loop in form in django Templates 
### 1. For loop in Visible fields

# creating form class

## `StudentRegistration` Form


```python
# forms.py

class StudentRegistration(forms.Form):
    """
    Django form for student registration.

    Fields:
    - `name` (CharField): Field for the name of the student.
    - `stu_gender` (ChoiceField): Field for the gender of the student, displayed as radio buttons.
    - `age` (IntegerField): Field for the age of the student.
    - `email` (EmailField): Field for the email address of the student.
    """

    name = forms.CharField()
    stu_gender = forms.ChoiceField(
        choices=gender,
        required=True,
        widget=forms.RadioSelect
    )
    age = forms.IntegerField()
    email = forms.EmailField()

```


### Templates file

```html

# # Student Details  
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Details</title>
    <style>
        body {
            background-color: rgba(0, 0, 0, 0.603);
            color: white;
        }
    </style>
</head>

<body>
    <!-- this for visible fields  -->
   <form action="" method="get">
        {% csrf_token %}

        {% for field in form %}
        {{field.label_tag}}
        <br>
        {{field}}
        <br>
        {% endfor %}

    </form> 

</body>

</html>

```
### 2. Hidden Fileds 

```python
# views.py 
class StudentRegistration(forms.Form):
    name = forms.CharField()
    stu_gender = forms.ChoiceField(
        choices=gender,
        required=True,
        widget=forms.RadioSelect
    )
    age = forms.IntegerField()
    email = forms.EmailField()
    key = forms.CharField(widget=forms.HiddenInput())

 ```

 ### Templates files
 ```html 


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Details</title>
    <style>
        body {
            background-color: rgba(0, 0, 0, 0.603);
            color: white;
        }
    </style>
</head>

<body>
 

    <!-- for hidden fileds  -->
    <form action="" method="get">
        {% csrf_token %}


        {% for field in form.visible_fields %}
        {{field.label_tag}}
        <br>
        {{field}}
        <br>
        {% endfor %}
        <input type="submit" value="Submit">
    </form>
</body>

</html>

 ```

