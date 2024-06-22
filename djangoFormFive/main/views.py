from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.


def index(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            age = fm.cleaned_data['age']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']

            print("name: ", name)
            print("age: ", age)
            print("email: ", email)
            print("password: ", password)

    else:
        fm = StudentRegistration()
    return render(request, 'main/index.html', {'form': fm})
