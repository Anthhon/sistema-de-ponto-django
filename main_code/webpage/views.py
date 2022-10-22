# from django.views.generic import DetailView, ListView
from .models import CheckIn, Funcionario
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse


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

    checkins = paginator.get_page(page)

    return render(request, 'employees-info.html', {'employee_info': employee_info, 'checkins': checkins})

def postCheckin(request):
    if request.method == 'POST':
        if 'entrada_manha' in request.POST:
            return HttpResponse('<h1>Entrada manhã funcionando</h1>')
        elif 'saida_manha' in request.POST:
            return HttpResponse('<h1>Saida manhã funcionando</h1>')
        elif 'entrada_tarde' in request.POST:
            return HttpResponse('<h1>Entrada tarde funcionando</h1>')
        elif 'saida_tarde' in request.POST:
            return HttpResponse('<h1>Saída tarde funcionando</h1>')
