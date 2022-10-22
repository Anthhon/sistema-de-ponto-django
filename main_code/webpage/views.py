import datetime
from .models import CheckIn, Funcionario
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from datetime import timedelta

def mainPage(request):
    employees = Funcionario.objects.all()
    return render(request, 'index.html', {'employees':employees})

def homePage(request):
    return render(request, 'mainpage.html')

def aboutPage(request):
    return render(request, 'about.html')

def employeesPage(request):
    employees_list = Funcionario.objects.all().order_by('nome')

    paginator = Paginator(employees_list, 6)

    page = request.GET.get('page')

    employees = paginator.get_page(page)

    return render(request, 'employees.html', {'employees': employees})

def detailEmployees(request, id):
    employee_info = get_object_or_404(Funcionario, pk=id)
    
    checkin_list = CheckIn.objects.filter(funcionario=employee_info).order_by('-dia')

    paginator = Paginator(checkin_list, 32)

    page = request.GET.get('page')
    
    horas_trabalhadas:timedelta
    for checkin in checkin_list:
        horas_trabalhadas = timedelta(days=0,hours=checkin.entrada_tarde.hour, minutes=checkin.saida_tarde.minute) - timedelta(days=0,hours=checkin.entrada_manha.hour,minutes=checkin.entrada_manha.minute)
        
    checkins = paginator.get_page(page)
    """ horas_trabalhadas:float = 0.0
    minutos_trabalhadas:float = 0.0
    for checkin in checkin_list:
        horas_trabalhadas =   checkin.entrada_manha.hour - checkin.saida_manha.hour
        minutos_trabalhadas = checkin.entrada_tarde.hour - checkin.saida_tarde.minute 
    horas_totais_trabalhadas:float = horas_trabalhadas + minutos_trabalhadas """
    """ horas_trabalhadas = ''
    minutos_trabalhadas = '' """

    return render(request, 'employees-info.html', {'employee_info': employee_info, 'checkins': checkins,'horas_trabalhadas':horas_trabalhadas})