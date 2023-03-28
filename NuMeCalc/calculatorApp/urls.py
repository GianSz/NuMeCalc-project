from django.urls import path
from .views import selectionPage, calculatorPage

app_name = 'calculatorApp'
urlpatterns = [
    path('', selectionPage, name='selectionPage'),
    path('calculator', calculatorPage, name='calculatorPage'),
]