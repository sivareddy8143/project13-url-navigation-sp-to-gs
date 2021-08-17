from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_siva(request):
    return render(request,'app1_siva.html')

def app_string(request):
    return HttpResponse('app_string')
