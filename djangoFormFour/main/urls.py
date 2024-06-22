from django.urls import path
from .views import showstudentdata

urlpatterns = [
    path('', showstudentdata, name='showdata'),
]
