from django.urls import path
from . import views

app_name = 'calculatorApp'
urlpatterns = [
    path('', views.selectionPage, name='selectionPage'),
    path('biseccion/', views.biseccion, name='biseccion'),
    path('puntoFijo/', views.puntoFijo, name='puntoFijo'),
    path('secante/', views.secante, name='secante'),
    path('newtonRaph/', views.newtonRaph, name='newtonRaph'),
    path('newtonRaph2/', views.newtonRaph2, name='newtonRaph2'),
    #capitulo 2
    path('goMatrix/<int:method>', views.goMatrix, name='goMatrix'),
    path('jacobi/', views.matJacobiSeidSor, name='jacobi'),
    path('gaussSeid/', views.matJacobiSeidSor, name='gaussSeid'),
    path('sor/', views.matJacobiSeidSor, name='sor'),
    path('sysEq/', views.matJacobiSeidSor, name='sysEq'),
    #capitulo 3
    path('vandermonde/', views.vandermonde, name='vandermonde')
]