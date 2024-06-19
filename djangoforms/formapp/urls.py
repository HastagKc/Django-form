from django.urls import path

from .views import studentReg

urlpatterns = [
    path("", studentReg, name='studentReg'),
]
