

from django.urls import path
from django.urls import re_path

from . import views

urlpatterns=[
    path('questions/<int:num>/',views.get_num_of_questions)
]
