from unicodedata import name


from django.urls import path


from . import views

from .views import aboutPage, colaboradores, homePage, mainPage

app_name = "webpage"



urlpatterns = [
    path('', mainPage, name='webpage-view'),
    path('entenda-melhor/', homePage, name='homepage-view'),
    path('sobre/', aboutPage, name='aboutpage-view'),
    path('colaboradores/',colaboradores,name='colaboradores'),
    path('',views.aboutPage)
]