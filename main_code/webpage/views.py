from django.urls import reverse
from django.http import HttpResponse
from .models import CheckIn, Funcionario
from django.core.paginator import Paginator
from datetime import datetime, time, timedelta
from django.shortcuts import get_object_or_404, redirect, render

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
    # Solicita as informações do colaborador
    employee_info = get_object_or_404(Funcionario, pk=id)
    
    # Solicita e limita as informações do colaborador especificado
    checkin_list = CheckIn.objects.filter(funcionario=employee_info).order_by('-dia')
    paginator = Paginator(checkin_list, 32) # Tempo de carreira a ser mostrado
    page = request.GET.get('page')
    checkins = paginator.get_page(page)
    
    # Calcula o tempo de carreira do especificado na paginação
    horas_trabalhadas = sum((checkin.saida_manha.hour - checkin.entrada_manha.hour) + (checkin.saida_tarde.hour - checkin.entrada_tarde.hour) for checkin in checkin_list)
    minutos_trabalhadas = sum((checkin.saida_manha.minute - checkin.entrada_manha.minute) + (checkin.saida_tarde.minute - checkin.entrada_tarde.minute) for checkin in checkin_list)
    horas_totais_trabalhadas = timedelta(days=0,hours=horas_trabalhadas,minutes=minutos_trabalhadas)
    
    # Formata o tempo calculado para exibição
    horas_teste = str(horas_totais_trabalhadas)
    tempo_array = horas_teste.split(':')
    tempo_real = f"{tempo_array[0]} Horas e {tempo_array[1]} Minutos"

    return render(request, 'employees-info.html', {'employee_info': employee_info, 'checkins': checkins, 'horas_trabalhadas':tempo_real})

def register_time_employee(request,*args, **kwargs):
    funcionario = Funcionario.objects.get(id=request.POST.get('employees'))
    horario = request.POST.get('horario')
    horas = int(horario[0:2])
    minutos = int(horario[3:5])
        
    if request.POST.get('entrada-manha') is not None:
        checkin, criado = CheckIn.objects.get_or_create(funcionario=funcionario,dia=datetime.now())
        checkin.entrada_manha = time(hour=horas,minute=minutos)
        checkin.save()
    if request.POST.get('entrada-tarde') is not None:
        checkin, criado = CheckIn.objects.get_or_create(funcionario=funcionario,dia=datetime.now())
        checkin.entrada_tarde = time(hour=horas,minute=minutos)
        checkin.save()
    if request.POST.get('saida-manha') is not None:
        checkin, criado = CheckIn.objects.get_or_create(funcionario=funcionario,dia=datetime.now())
        checkin.saida_manha = time(hour=horas,minute=minutos)
        checkin.save()
    if request.POST.get('saida-tarde') is not None:
        checkin, criado = CheckIn.objects.get_or_create(funcionario=funcionario,dia=datetime.now())
        checkin.saida_tarde = time(hour=horas,minute=minutos)
        checkin.save()
        
    return redirect(reverse('webpage:webpage-view'))
