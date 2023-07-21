from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'crm/index.html', {})


def register(request):
    return render(request, 'crm/register.html', {})


def loginPage(request):
    return render(request, 'crm/login.html', {})

def dashboard(request):
    return render(request, 'crm/dashboard.html', {})
