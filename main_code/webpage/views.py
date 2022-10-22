from django.http import HttpResponse
from django.urls import reverse
from .models import CheckIn, Funcionario
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime, time, timedelta

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
    
    horas_trabalhadas = sum((checkin.saida_manha.hour - checkin.entrada_manha.hour) + (checkin.saida_tarde.hour - checkin.entrada_tarde.hour) for checkin in checkin_list)
    minutos_trabalhadas = sum((checkin.saida_manha.minute - checkin.entrada_manha.minute) + (checkin.saida_tarde.minute - checkin.entrada_tarde.minute) for checkin in checkin_list)
    horas_totais_trabalhadas = f'{horas_trabalhadas} horas :{minutos_trabalhadas} minutos' #SE QUISER FORMATO EM HORAS TOTAIS, USE ESSE
    #horas_totais_trabalhadas = timedelta(days=0,hours=horas_trabalhadas,minutes=minutos_trabalhadas) #SE VC QUISER EM FORMATO DIAS, USE ESSE
    
    checkins = paginator.get_page(page)

    return render(request, 'employees-info.html', {'employee_info': employee_info, 'checkins': checkins,'horas_trabalhadas':horas_totais_trabalhadas})


def register_time_employee(request,*args, **kwargs):
    MESSAGEM_ERROR = "Horario ja configurado, se quiser alterar visite o painel de administração!"
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