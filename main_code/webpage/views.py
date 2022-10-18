from .models import Funcionario
from django.shortcuts import render, get_object_or_404

# Create your views here.
def mainPage(request):
    return render(request, 'index.html')

def homePage(request):
    return render(request, 'mainpage.html')

def aboutPage(request):
    return render(request, 'about.html')

def employeesPage(request):
    employees = Funcionario.objects.all()
    return render(request, 'employees.html', {'employees': employees})