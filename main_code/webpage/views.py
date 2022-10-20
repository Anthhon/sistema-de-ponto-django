from django.shortcuts import get_object_or_404, render
# from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator
from .models import Funcionario

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
    return render(request, 'employees-info.html', {'employee_info': employee_info})
    



# class EployeesTemplateListView(ListView):
#     paginator_class = Paginator
#     #paginate_orphans = 1
#     model = Funcionario
#     template_name = TEMPLATE_EMPLOYEES_PATH
#     paginate_by = 1
#     context_object_name = "employees"
    
#     """ def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["employees"] = self.paginator_class
#         return context """
    
    
# class ModelDetailView(DetailView):
#     model = Funcionario
#     template_name = "funcionario-detalhe.html"
    

    
