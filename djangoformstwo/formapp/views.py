from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.


def studentReg(request):
    # create object
    # fm = StudentRegistration()
    # changing the name of the id attribute using django
    # fm = StudentRegistration(auto_id="student_%s", label_suffix=" ")

    # adding initial form in input
    fm = StudentRegistration(
        initial={
            'name': 'Kshittiz Chaudhary', 'age': 25, 'email': 'chaudharykshittiz950@gmail.com'
        }
    )
    # rearranging the fields of the form in templates file using django method
    # this method is use to rearrange the field in django
    fm.order_fields(field_order=['name', 'age', 'stu_gender', 'email'])
    return render(request, 'formapp/studentDetails.html', {'form': fm})
