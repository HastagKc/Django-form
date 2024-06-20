from django import forms


gender = [
    ('male', 'male'),
    ('female', 'female'),
    ('None', 'Prefer Not to say'),
]

# creating form class


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
