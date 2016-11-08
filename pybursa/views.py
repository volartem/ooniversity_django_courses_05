from django.http import HttpResponse, response
from django.shortcuts import render

def index(request):
    print('request', request)
    return render(request, "index.html")

def contact(request):
    print('request', request)
    return render(request, "contact.html")

def student_list(request):
    print('request', request)
    return render(request, "student_list.html")

def student_detail(request):
    print('request', request)
    return render(request, "student_detail.html")