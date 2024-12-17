from django.http import HttpResponse
from django.template import loader

def home(request):
  return HttpResponse('home.html')    