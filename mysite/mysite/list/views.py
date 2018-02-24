from django.shortcuts import render
from django.http import HttpResponse

def add(request,question_id):
	return HttpResponse("You're looking at question %s." % question_id)

# Create your views here.
