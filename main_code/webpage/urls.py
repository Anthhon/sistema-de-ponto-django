from unicodedata import name
from django.urls import path
from .views import mainPage, homePage, aboutPage, colaboradores
from . import views

app

urlpatterns = [
    path('', mainPage, name='webpage-view'),
    path('entenda-melhor/', homePage, name='homepage-view'),
    path('sobre/', aboutPage, name='aboutpage-view'),
    path('colaboradores/',colaboradores,name='colaboradores'),
    path('',views.aboutPage)
]