from django.shortcuts import render
import matlab.engine #Download this library by doing python -m pip install matlabengine
import pandas as pd

eng = matlab.engine.start_matlab() #opens matlab

# Create your views here.
def selectionPage(request):
    return render(request, 'calculatorApp/selectionPage.html', context={})

def calculatorPage(request):
    return render(request, 'calculatorApp/calculatorPage.html', context={})

def biseccion(request):
    #Arguments we need to do the function
    xi = 2.0   #Be careful to put all these data in float type!
    xs = 3.0
    tol = 0.005
    typeTol = 0
    niter = 100.0 
    #fun = input() #read the function given
    eng.Biseccion(xi,xs,tol,typeTol,niter) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
    df = pd.read_csv('biseccion.csv')
    print(df)
    render(request, 'calculatorApp/biseccion.html',context={})
