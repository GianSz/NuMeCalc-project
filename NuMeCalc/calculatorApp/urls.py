from django.urls import path
from . import views

app_name = 'calculatorApp'
urlpatterns = [
    path('', views.selectionPage, name='selectionPage'),
    path('calculator', views.calculatorPage, name='calculatorPage'),
    path('biseccion/', views.biseccion, name='biseccion'),
    path('secante/', views.secante, name='secante'),
    path('newtonRaph/', views.newtonRaph, name='newtonRaph'),
    #capitulo 2
    path('goMatrix/<int:method>', views.goMatrix, name='goMatrix'),
    path('jacobi/', views.matJacobiSeidSor, name='jacobi'),
    path('gaussSeid/', views.matJacobiSeidSor, name='gaussSeid'),
    path('sor/', views.matJacobiSeidSor, name='sor'),
    path('sysEq/', views.matJacobiSeidSor, name='sysEq'),
    #capitulo 3
]