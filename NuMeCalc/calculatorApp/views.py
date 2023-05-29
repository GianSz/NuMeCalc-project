from django.shortcuts import render,redirect
from django.contrib import messages
import matlab.engine #Download this library by doing python -m pip install matlabengine
import pandas as pd

from NuMeCalc.settings import BASE_DIR
import os

eng = matlab.engine.start_matlab() #opens matlab

# Create your views here.
def selectionPage(request):
    return render(request, 'calculatorApp/selectionPage.html', context={})
# -----------------------------------------Capítulo 1--------------------------------------------------------

def biseccion(request):
    #Arguments we need to do the function
    xi = -1.0   #Be careful to put all these data in float type!
    xs = 1.0
    tol = 0.005
    typeTol = 0
    # tipos:
    # - 0 -> dc
    # - 1 -> cs
    niter = 100.0 
    fun = '(x^2)-1' #read the function given
    T = eng.code_biseccion(xi,xs,tol,typeTol,niter,fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
    if(T == 'El intervalo es inadecuado' or ('es raiz de f(x)' in T)):
        print(T)
    else:
        df = pd.read_csv('data_biseccion.csv')
        print(df)
    return render(request, 'calculatorApp/biseccion.html',context={})

def puntoFijo(request):
    #Arguments we need to do the function
    
    x0 = 0
    tol = 0.005
    typeTol = 0
    # tipos:
    # - 0 -> dc
    # - 1 -> cs
    niter = 100.0
    fun = '2*(exp(1)^(x^2))-5*x'
    funG = '(2*(exp(1)^(x^2)))/5'
    T = eng.code_puntoFijo(x0, tol, typeTol, niter, fun, funG)
    
    return render(request, 'calculatorApp/puntoFijo.html', context={})

def secante(request):
    #Arguments we need to do the function
    x0 = 3.0   #Be careful to put all these data in float type!
    x1 = 3.5
    tol = 0.005
    typeTol = 0
    # tipos:
    # - 0 -> dc
    # - 1 -> cs
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
    # tipos:
    # - 0 -> dc
    # - 1 -> cs
    niter = 100.0 
    fun = '(x^3+5)-2' #read the function given
    eng.code_newtonRaph(x0,tol,typeTol,niter,fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
    df = pd.read_csv('data_newtonRaph.csv')
    print(df)
    return render(request, 'calculatorApp/secante.html',context={})

def newtonRaph2(request):
    #Arguments we need to do the function
    x0 = 0  #Be careful to put all these data in float type!
    tol = 0.005
    typeTol = 0
    # tipos:
    # - 0 -> dc
    # - 1 -> cs
    niter = 100.0
    fun = '2*(exp(1)^(x^2))-5*x'
    T = eng.code_newtonRaph2(x0, tol, typeTol, niter, fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code

    return render(request, 'calculatorApp/newtonRaph2.html', context={})
# -----------------------------------------Capítulo 2--------------------------------------------------------

def goMatrix(request,method):
    if(method==0):
        return render(request,'calculatorApp/cap2-selNxN.html',context={'method':'jacobi'})
    elif(method==1):
        return render(request,'calculatorApp/cap2-selNxN.html',context={'method':'gaussSeid'})
    elif(method==2):
        return render(request,'calculatorApp/cap2-selNxN.html',context={'method':'sor'})
    else:
        messages.error(request,"Estas ingresando incorrectamente a un metodo matricial")
        return redirect('selectionPage')

def matJacobiSeidSor(request):
    #Arguments we need to do the function
    tol = 0.005
    typeTol = 0
    # tipos:
    # - 0 -> dc
    # - 1 -> cs
    niter = 1000.0 
    met=2
    # métodos:
    # - 0 -> jacobi
    # - 1 -> gauss-seidel
    # - 2 -> SOR
    w=0.5
    eng.code_MatJacobiSeidSor(tol,typeTol,niter,met,w) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
    df = pd.read_csv('data_iterativos.csv')
    print(df)
    return render(request, 'calculatorApp/biseccion.html',context={})

# -----------------------------------------Capítulo 3--------------------------------------------------------
def vandermonde(request):
    x_list = request.POST[x_list].split(sep=',')
    y_list = request.POST[y_list].split(sep=',')

    file_pathA = os.path.join(BASE_DIR, 'matrix-A_vandermonde.txt')
    if(os.path.isfile(file_pathA)):
        os.remove(file_pathA)

    file_pathb = os.path.join(BASE_DIR, 'matrix-b_vandermonde.txt')
    if(os.path.isfile(file_pathb)):
        os.remove(file_pathb)

    archivo1 = open('matrix-A_vandermonde.txt', 'w')
    archivo2 = open('matrix-b_vandermonde.txt', 'w')

    for i,x in enumerate(x_list):
        x = int(x)
        count = len(x_list)-1
        while(count>=0):
            if count==0:
                archivo1.write(f'1')
                break
            archivo1.write(f'{x**count},')
            count-=1
        if(i==len(x_list)-1):
            break
        archivo1.write('\n')
    
    for i,y in enumerate(y_list):
        if(i==len(y_list)-1):
            archivo2.write(y)
            break
        archivo2.write(f'{y}\n')

    eng.code_vandermonde()
    return render(request, 'calculatorApp/vandermonde.html', context={})

def moveData(image_name, csv_name):
    file_path = os.path.join(BASE_DIR, image_name)
    destination_path = os.path.join(BASE_DIR, 'calculatorApp', 'static', 'images', image_name)
    os.rename(file_path, destination_path)

    file_path = os.path.join(BASE_DIR, csv_name)
    destination_path = os.path.join(BASE_DIR, 'calculatorApp', 'static', 'csv', csv_name)
    os.rename(file_path, destination_path)