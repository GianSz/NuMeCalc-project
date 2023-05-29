from django.shortcuts import render,redirect
from django.contrib import messages
import matlab.engine #Download this library by doing python -m pip install matlabengine
import pandas as pd

eng = matlab.engine.start_matlab() #opens matlab

# Create your views here.
def selectionPage(request):
    return render(request, 'calculatorApp/selectionPage.html', context={})

def calculatorPage(request):
    return render(request, 'calculatorApp/calculatorPage.html', context={})
# -----------------------------------------Capítulo 1--------------------------------------------------------

def biseccion(request):
    if (request.method == 'POST'):
        #Arguments we need to do the function
        xi = request.POST.get('inicioInt')   #Be careful to put all these data in float type!
        xs = request.POST.get('finInt')
        tol = request.POST.get('tolerancia')
        typeTol = request.POST.get('tipoError')
        niter = request.POST.get('niter')
        fun = request.POST.get('funcion') #read the function given
        eng.code_biseccion(float(xi),float(xs),float(tol),float(typeTol),float(niter),fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
        csv_file = open('data_biseccion.csv', 'r')
        data = csv_file.readlines()
        columnNames = data[0].split(',')
        columnNames[len(columnNames)-1] = columnNames[len(columnNames)-1].replace('\n','')
        table = []
        for i in range(1, len(data)):
            row = data[i].split(',')
            row[len(row)-1] = row[len(row)-1].replace('\n','')
            table.append(row)
        if(float(table[len(table)-1][3])<= float(tol)):
            sol = table[len(table)-1][1]
        else:
            sol="No se llegó a la respuesta esperada con " + niter + " iteraciones"
        return render(request, 'calculatorApp/biseccion.html',context={'tablaIter':table,'title':columnNames,'sol':sol})
    
    return render(request, 'calculatorApp/biseccion.html',context={})

def secante(request):
    if(request.method == 'POST'):
        #Arguments we need to do the function
        x0 = request.POST.get('x0')   #Be careful to put all these data in float type!
        x1 = request.POST.get('x1')
        tol = request.POST.get('tolerancia')
        typeTol = request.POST.get('tipoError')
        niter = request.POST.get('niter') 
        fun = request.POST.get('funcion') #read the function given
        eng.code_secante(float(x0),float(x1),float(tol),float(typeTol),float(niter),fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
        csv_file = open('data_secante.csv', 'r')
        data = csv_file.readlines()
        columnNames = data[0].split(',')
        columnNames[len(columnNames)-1] = columnNames[len(columnNames)-1].replace('\n','')
        table = []
        for i in range(1, len(data)):
            row = data[i].split(',')
            row[len(row)-1] = row[len(row)-1].replace('\n','')
            table.append(row)
        if(float(table[len(table)-1][3])<= float(tol)):
            sol = table[len(table)-1][1]
        else:
            sol="No se llegó a la respuesta esperada con " + niter + " iteraciones"
        return render(request, 'calculatorApp/secante.html',context={'tablaIter':table,'title':columnNames,'sol':sol})
    return render(request, 'calculatorApp/secante.html',context={})

def newtonRaph(request):
    if (request.method == 'POST'):
        #Arguments we need to do the function
        x0 = request.POST.get('x0')   #Be careful to put all these data in float type!
        tol = request.POST.get('tolerancia')
        typeTol = request.POST.get('tipoError')
        niter = request.POST.get('niter')
        fun = request.POST.get('funcion') #read the function given
        eng.code_newtonRaph(float(x0),float(tol),float(typeTol),float(niter),fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
        csv_file = open('data_newtonRaph.csv', 'r')
        data = csv_file.readlines()
        columnNames = data[0].split(',')
        columnNames[len(columnNames)-1] = columnNames[len(columnNames)-1].replace('\n','')
        table = []
        for i in range(1, len(data)):
            row = data[i].split(',')
            row[len(row)-1] = row[len(row)-1].replace('\n','')
            table.append(row)
            
        if(float(table[len(table)-1][3])<= float(tol)):
            sol = table[len(table)-1][1]
        else:
            sol="No se llegó a la respuesta esperada con " + niter + " iteraciones"

        return render(request, 'calculatorApp/newtonRaph.html',context={'tablaIter':table,'title':columnNames,'sol':sol})
    
    return render(request, 'calculatorApp/newtonRaph.html',context={})

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
