from django.urls import path
from .views import student_view, success
urlpatterns = [
    path('', student_view, name='student_view'),
    path('success/', success, name='success'),
]
