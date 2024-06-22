from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.


def showstudentdata(request):
    if request.method == "POST":
        # create object of form class
        fm = StudentRegistration(request.post)
        if fm.is_valid():
            print("Form is valid ")
            print(f'name: {fm.cleaned_data["name"]}')
            print(f'email: {fm.cleaned_data["email"]}')

        else:
            fm = StudentRegistration()

    return render(request, 'main/studentform.html', {'form': fm})
 