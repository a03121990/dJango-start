from django.shortcuts import render ,HttpResponse

def index(request):
    return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is aboutpage")

def contact(request):
    return HttpResponse("this is contactpage")

def services(request):
    return HttpResponse("this is service page")

