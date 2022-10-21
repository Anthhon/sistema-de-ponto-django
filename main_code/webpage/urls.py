# from unicodedata import name

from django.urls import path

from .views import (aboutPage, detailEmployees, employeesPage, homePage, mainPage, postCheckin)

app_name = "webpage"

urlpatterns = [
    path('', mainPage, name='webpage-view'),
    path('entenda-melhor/', homePage, name='homepage-view'),
    path('sobre/', aboutPage, name='aboutpage-view'),
    path('colaborador/',employeesPage,name='employeespage-view'),
    path('colaborador-info/<int:id>', detailEmployees, name='employeeinfo-view'),
    path('adicionando-horario/', postCheckin, name="post-checkin")
]