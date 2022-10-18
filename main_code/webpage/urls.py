from unicodedata import name
from django.urls import path
from .views import mainPage, homePage, aboutPage, employeesPage

app_name = 'webpage'

urlpatterns = [
    path('', mainPage, name='webpage-view'),
    path('entenda-melhor/', homePage, name='homepage-view'),
    path('sobre/', aboutPage, name='aboutpage-view'),
    path('colaboradores/', employeesPage, name='employeespage-view'),
]