from django.shortcuts import render

# Create your views here.
def selectionPage(request):
    return render(request, 'calculatorApp/selectionPage.html', context={})

def calculatorPage(request):
    return render(request, 'calculatorApp/calculatorPage.html', context={})