# from django.views.generic import DetailView, ListView
import datetime
from .models import CheckIn, Funcionario
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render


def mainPage(request):
    employees = Funcionario.objects.all()
    return render(request, 'index.html', {'employees':employees})

def homePage(request):
    return render(request, 'mainpage.html')

def aboutPage(request):
    return render(request, 'about.html')

def employeesPage(request):
    employees_list = Funcionario.objects.all()

    paginator = Paginator(employees_list, 6)

    page = request.GET.get('page')

    employees = paginator.get_page(page)

    return render(request, 'employees.html', {'employees': employees})

def detailEmployees(request, id):
    employee_info = get_object_or_404(Funcionario, pk=id)
    
    checkin_list = CheckIn.objects.filter(funcionario=employee_info).order_by('-dia')

    paginator = Paginator(checkin_list, 32)

    page = request.GET.get('page')

    checkins = paginator.get_page(page)

    return render(request, 'employees-info.html', {'employee_info': employee_info, 'checkins': checkins})