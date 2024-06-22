from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    # validation specifies files
    def clean_age(self):
        age_data = self.cleaned_data['age']
        if age_data < 0:
            raise forms.ValidationError("Age can't be negative ")
        return age_data
