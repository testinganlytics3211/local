from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request, 'testapp/home.html')


def About(request):
    return render(request, 'testapp/about.html')
