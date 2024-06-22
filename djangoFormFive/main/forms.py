from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    # validation specifies field
    # def clean_age(self):
    #     age_data = self.cleaned_data['age']
    #     if age_data < 0:
    #         raise forms.ValidationError("Age can't be negative ")
    #     return age_data

 # Validate all fields
    def clean(self):
        cleaned_data = super().clean()
        valname = cleaned_data.get('name')
        valage = cleaned_data.get('age')

        if valname and len(valname) < 2:
            raise forms.ValidationError("Name can't be less than 2 characters")

        if valage is not None and valage < 0:
            raise forms.ValidationError("Age can't be negative")

        return cleaned_data
