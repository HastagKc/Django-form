from django.shortcuts import render, redirect
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.


def success(request):
    return render(request, 'main/success.html')


def showstudentdata(request):
    if request.method == "POST":
        # create object of form class
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Form is valid ")
            print(f'name: {fm.cleaned_data["name"]}')
            print(f'email: {fm.cleaned_data["email"]}')
            # return redirect('main/success.html')
            return HttpResponseRedirect('/success/')

    else:
        fm = StudentRegistration()

    return render(request, 'main/studentform.html', {'form': fm})
