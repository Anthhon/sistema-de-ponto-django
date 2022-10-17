from django.urls import path
from .views import mainPage

urlpatterns = [
    path('', mainPage, name='webpage-view'),
]