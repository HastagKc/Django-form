from django.shortcuts import render, redirect
from .forms import StudentRegistrationFrom
# Create your views here.


def student_view(request):

    if request.method == 'POST':
        # HERE form comes with some data
        fm = StudentRegistrationFrom(request.POST)
        if fm.is_valid():
            return redirect('success')

    else:
        # creating empty form by creating object of StudentRegistrationFrom
        fm = StudentRegistrationFrom()
    return render(request, 'base/index.html', {'form': fm})


def success(request):
    return render(request, 'base/success.html')
