from django.shortcuts import render
from .models import SingleQuestion
from django.core import serializers
from django.http import HttpResponse

def get_num_of_questions(request,num):
    print('into get num of questions: ', num)
    count = num
    questions = ''
    acutal_count = SingleQuestion.objects.all().count()
    print(acutal_count)
    if count < acutal_count:
        questions = SingleQuestion.objects[:count]
    else:
        questions = SingleQuestion.objects.all()
    data = serializers.serialize('json',questions)
    print(data)
    return HttpResponse('hello questions') 
