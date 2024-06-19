from django import forms


gender = [
    ('male', 'male'),
    ('female', 'female'),
    ('None', 'Prefer Not to say'),
]

# creating form class


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    age = forms.IntegerField()
    stu_gender = forms.ChoiceField(
        choices=gender,
        required=True,
        widget=forms.RadioSelect
    )
