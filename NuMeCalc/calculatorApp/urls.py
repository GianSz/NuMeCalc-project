from django.urls import path
from . import views

app_name = 'calculatorApp'
urlpatterns = [
    path('', views.selectionPage, name='selectionPage'),
    path('biseccion/', views.biseccion, name='biseccion'),
    path('reglaFalsa/',views.reglaFalsa,name='reglaFalsa'),
    path('puntoFijo/', views.puntoFijo, name='puntoFijo'),
    path('secante/', views.secante, name='secante'),
    path('newtonRaph/', views.newtonRaph, name='newtonRaph'),
    path('newtonRaph2/', views.newtonRaph2, name='newtonRaph2'),
    #capitulo 2
    path('goMatrix/<int:method>/', views.goMatrix, name='goMatrix'),
    path('introMatrix/<int:method>/', views.introMatrix, name='introMatrix'),
    path('sysEq/', views.matJacobiSeidSor, name='sysEq'),
    #capitulo 3
    path('newtonInter/',views.newtonInter, name = 'newtonInter'),
    path('vandermonde/', views.vandermonde, name='vandermonde'),
    path('splineLineal/',views.splineLineal, name = 'splineLineal'),
    path('splineCubico/',views.splineCubico, name = 'splineCubico'),
    path('api/sendPoints', views.sendPoints, name='sendPoints'),
    path('newton1/', views.newton1, name='newton1'),
]