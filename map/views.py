from django.shortcuts import render
from django.http import HttpResponse

def map(request):
  return HttpResponse("Map page")