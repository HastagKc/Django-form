from django.urls import path
from .views import showstudentdata, success

urlpatterns = [
    path('', showstudentdata, name='showdata'),
    path('success/', success, name='success'),
]
