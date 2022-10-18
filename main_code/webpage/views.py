from django.shortcuts import render

# Create your views here.
def mainPage(request):
    return render(request, 'index.html')

def homePage(request):
    return render(request, 'mainpage.html')

def aboutPage(request):
    return render(request, 'about.html')

def employeesPage(request):
    return render(request, 'employees.html')