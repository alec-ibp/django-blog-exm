from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def general(request):
    return render(request, "general.html")


def technology(request):
    return render(request, "technology.html")


def tutorials(request):
    return render(request, "tutorials.html")


def contact(request):
    return render(request, "contact.html")