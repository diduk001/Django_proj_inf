from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def details(request, question_id):
    return HttpResponse(f"You're looking at the details of question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You're looknig at the results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")