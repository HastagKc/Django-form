from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.


def studentReg(request):
    # create object
    fm = StudentRegistration()
    return render(request, 'formapp/studentDetails.html', {'form': fm})
