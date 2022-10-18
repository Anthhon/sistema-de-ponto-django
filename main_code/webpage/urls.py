from unicodedata import name

from django.urls import path

from . import views
from .views import (aboutPage, detailEmployees, employeesPage, homePage,
                    mainPage)

app_name = "webpage"

urlpatterns = [
    path('', mainPage, name='webpage-view'),
    path('entenda-melhor/', homePage, name='homepage-view'),
    path('sobre/', aboutPage, name='aboutpage-view'),
    path('employeesPage/',employeesPage,name='employeespage-view'),
    path('employees-detail/<slug:id_funcionario>',detailEmployees,name='detailEmployees'),
    path('',views.aboutPage),
]