from django.shortcuts import render
import matlab.engine #Download this library by doing python -m pip install matlabengine
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
eng = matlab.engine.start_matlab() #opens matlab
import json
# Create your views here.
def selectionPage(request):
    return render(request, 'calculatorApp/selectionPage.html', context={})

def calculatorPage(request):
    return render(request, 'calculatorApp/calculatorPage.html', context={})
# -----------------------------------------Capítulo 1--------------------------------------------------------

def biseccion(request):
    #Arguments we need to do the function
    xi = 2.0   #Be careful to put all these data in float type!
    xs = 3.0
    tol = 0.005
    typeTol = 0
    niter = 100.0 
    fun = '(x^3+5)-2' #read the function given
    eng.code_biseccion(xi,xs,tol,typeTol,niter,fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
    df = pd.read_csv('data_biseccion.csv')
    print(df)
    return render(request, 'calculatorApp/biseccion.html',context={})

def secante(request):
    #Arguments we need to do the function
    x0 = 3.0   #Be careful to put all these data in float type!
    x1 = 3.5
    tol = 0.005
    typeTol = 0
    niter = 100.0 
    fun = '(x^3+5)-2' #read the function given
    eng.code_secante(x0,x1,tol,typeTol,niter,fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
    df = pd.read_csv('data_secante.csv')
    print(df)
    return render(request, 'calculatorApp/secante.html',context={})

def newtonRaph(request):
    #Arguments we need to do the function
    x0 = 3.0   #Be careful to put all these data in float type!
    tol = 0.005
    typeTol = 0
    niter = 100.0 
    fun = '(x^3+5)-2' #read the function given
    eng.code_newtonRaph(x0,tol,typeTol,niter,fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
    df = pd.read_csv('data_newtonRaph.csv')
    print(df)
    return render(request, 'calculatorApp/secante.html',context={})

# -----------------------------------------Capítulo 2--------------------------------------------------------

def sor(request):
    return render(request,'calculatorApp/sor.html',context={})


# -----------------------------------------Capítulo 3--------------------------------------------------------
def splineLineal(request):
    return render(request,'calculatorApp/splineLineal.html',context={})
def splineCubico(request):
    return render(request,'calculatorApp/splineCubico.html',context={})

@csrf_exempt
def sendPoints(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        x = json.loads(data['x'])
        y = json.loads(data['y'])
        d = json.loads(data['d'])
        print("points: ")
        print(x)
        print(y)
        print(d)

        response_data = {
            'points': "received",
        }
        eng.Spline(x,y,d) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
        df = pd.read_csv('data_Spline.csv')
        print(df)
        return  JsonResponse(response_data,safe = False)
    else:
        return JsonResponse({'error': 'Invalid request method'})