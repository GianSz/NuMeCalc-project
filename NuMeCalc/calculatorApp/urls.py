from django.urls import path
from . import views

app_name = 'calculatorApp'
urlpatterns = [
    path('', views.selectionPage, name='selectionPage'),
    path('calculator', views.calculatorPage, name='calculatorPage'),
    path('biseccion/', views.biseccion, name='biseccion'),
    path('secante/', views.secante, name='secante'),
]