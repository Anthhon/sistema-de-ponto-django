from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Funcionario

TEMPLATE_EMPLOYEES_PATH = "employees.html"
# Create your views here.
def mainPage(request):
    return render(request, 'index.html')

def homePage(request):
    return render(request, 'mainpage.html')

def aboutPage(request):
    return render(request, 'about.html')


def employeesPage(request):
    employees_list = Funcionario.objects.all()

    paginator = Paginator(employees_list, 1)

    page = request.GET.get('page')

    employees = paginator.get_page(page)

    return render(request, 'employees.html', {'employees': employees})


def detailEmployees(request, id_funcionario):
    funcionario = Funcionario.objects.get(id=id_funcionario)
    """ alterar para get_object para o antony """
    TEMPLATE_DETAIL_EMPLYOEES_PATH = 'funcionario-detail.html'
    context = {'funcionario':funcionario}
    return render(request,TEMPLATE_DETAIL_EMPLYOEES_PATH,context)
    

class EployeesTemplateListView(ListView):
    paginator_class = Paginator
    #paginate_orphans = 1
    model = Funcionario
    template_name = TEMPLATE_EMPLOYEES_PATH
    paginate_by = 1
    context_object_name = "employees"
    
    """ def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["employees"] = self.paginator_class
        return context """
    
    
class ModelDetailView(DetailView):
    model = Funcionario
    template_name = "funcionario-detalhe.html"
    

    
