from django.shortcuts import render,redirect
from django.contrib import messages
import matlab.engine #Download this library by doing python -m pip install matlabengine
import pandas as pd

from NuMeCalc.settings import BASE_DIR
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

eng = matlab.engine.start_matlab() #opens matlab
import json
# Create your views here.
def selectionPage(request):
    return render(request, 'calculatorApp/selectionPage.html', context={})

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
        moveData('grafica_biseccion.png', 'data_biseccion.csv')

        columnNames, table, sol = getInfoTable('data_biseccion.csv', tol, niter)

        return render(request, 'calculatorApp/biseccion.html',context={'tablaIter':table,'title':columnNames,'sol':sol})
    
    return render(request, 'calculatorApp/biseccion.html',context={})

def reglaFalsa(request):
    if (request.method == 'POST'):
        #Arguments we need to do the function
        xi = request.POST.get('inicioInt')   #Be careful to put all these data in float type!
        xs = request.POST.get('finInt')
        tol = request.POST.get('tolerancia')
        typeTol = request.POST.get('tipoError')
        niter = request.POST.get('niter')
        fun = request.POST.get('funcion') #read the function given
        eng.code_ReglaFalsa(float(xi),float(xs),float(tol),float(typeTol),float(niter),fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
        csv_file = open('data_reglaFalsa.csv', 'r')
        data = csv_file.readlines()
        columnNames = data[0].split(',')
        columnNames[len(columnNames)-1] = columnNames[len(columnNames)-1].replace('\n','')
        table = []
        for i in range(1, len(data)):
            row = data[i].split(',')
            row[len(row)-1] = row[len(row)-1].replace('\n','')
            table.append(row)
        if(len(data[len(data)-1]) == 1):
            if data[1].replace('\n','') == "-1":
                sol = "Intervalo Inválido"
            else:
                resp = data[1].replace('\n','')
                sol = "falla en "+resp+" iteraciones"
        else:
            sol = "solución es "+table[len(table)-1][3]
        return render(request, 'calculatorApp/reglaFalsa.html',context={'tablaIter':table,'title':columnNames,'sol':sol})
    return render(request,'calculatorApp/reglaFalsa.html',context={})

def puntoFijo(request):
    #Arguments we need to do the function
    if(request.method == 'POST'):
        x0 = float(request.POST['x0'])
        tol = float(request.POST['tolerance'])
        typeTol = int(request.POST['typeTol'])
        # tipos:
        # - 0 -> dc
        # - 1 -> cs
        niter = int(request.POST['niter'])
        fun = request.POST['function']
        funG = request.POST['functionG']

        T = eng.code_puntoFijo(x0, tol, typeTol, niter, fun, funG)
        moveData('grafica_puntoFijo.png', 'data_puntoFijo.csv')

        columnNames, table, sol = getInfoTable('data_puntoFijo.csv', tol, niter)

        return render(request, 'calculatorApp/puntoFijo.html', context={'graph':True, 'title':columnNames, 'table':table,'sol':sol})
    
    return render(request, 'calculatorApp/puntoFijo.html', context={})

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
        moveData('grafica_secante.png', 'data_secante.csv')

        columnNames, table, sol = getInfoTable('data_secante.csv', tol, niter)

        return render(request, 'calculatorApp/secante.html', context={'graph':True, 'title':columnNames, 'table':table,'sol':sol})
    
    return render(request, 'calculatorApp/secante.html', context={})

def newtonRaph(request):
    if (request.method == 'POST'):
        #Arguments we need to do the function
        x0 = request.POST.get('x0')   #Be careful to put all these data in float type!
        tol = request.POST.get('tolerancia')
        typeTol = request.POST.get('tipoError')
        niter = request.POST.get('niter')
        fun = request.POST.get('funcion') #read the function given
        
        eng.code_newtonRaph(float(x0),float(tol),float(typeTol),float(niter),fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
        moveData('grafica_newtonRaph.png', 'data_newtonRaph.csv')

        columnNames, table, sol = getInfoTable('data_newtonRaph.csv', tol, niter)

        return render(request, 'calculatorApp/newtonRaph.html', context={'graph':True, 'title':columnNames, 'table':table,'sol':sol})
    
    return render(request, 'calculatorApp/newtonRaph.html', context={})

def newtonRaph2(request):
    if(request.method == 'POST'):
        #Arguments we need to do the function
        x0 = float(request.POST['x0'])
        tol = float(request.POST['tolerance'])
        typeTol = int(request.POST['typeTol'])
        # tipos:
        # - 0 -> dc
        # - 1 -> cs
        niter = int(request.POST['niter'])
        fun = request.POST['function']

        T = eng.code_newtonRaph2(x0, tol, typeTol, niter, fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
        moveData('grafica_newtonRaph2.png', 'data_newtonRaph2.csv')

        columnNames, table, sol = getInfoTable('data_newtonRaph2.csv', tol, niter)

        return render(request, 'calculatorApp/newtonRaph2.html', context={'graph':True, 'title':columnNames, 'table':table, 'sol':sol})

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

def introMatrix(request,method):
    if(method==0):
        method='jacobi'
    elif(method==1):
        method='gaussSeid'
    elif(method==2):
        method='sor'
    else:
        messages.error(request,"Estas ingresando incorrectamente a un metodo matricial")
        return redirect('selectionPage')
    
    n=int(request.POST.get('n'))
    gridDivR=range(1,n+2)
    gridDivC=range(1,n+4)

    return render(request,'calculatorApp/cap2-introMatrix.html',context={
        'method':method,
        'n':n,
        'ranN':range(1,n+1),
        'lim_n':n+1,
        'gridDivR':gridDivR,
        'gridDivC':gridDivC
        })

def matJacobiSeidSor(request):
    #extra arguments
    n=int(request.POST.get('n'))
    #create the txt
    #A
    matA=open('matrix-A.txt','w')
    for i in range(1,n+1):
        ln=""
        for j in range(1,n+1):
            a=float(request.POST.get('a'+str(i)+str(j)))
            ln+=str(a)+','
        ln+="\n"
        matA.write(ln)
    matA.close()
    #b
    matB=open('matrix-b.txt','w')
    for i in range(1,n+1):
        b=float(request.POST.get('a'+str(i)+str(n+2)))
        ln=str(b)+"\n"
        matB.write(ln)
    matB.close()
    #x0
    matX0=open('matrix-x0.txt','w')
    for i in range(1,n+1):
        x0=float(request.POST.get('a'+str(i)+str(n+3)))
        ln=str(x0)+"\n"
        matX0.write(ln)
    matX0.close()
    #Arguments we need to do the function
    tol = float(request.POST.get('tol'))
    typeTol = int(request.POST.get('typeTol'))
    # tipos:
    # - 0 -> dc
    # - 1 -> cs
    niter = int(request.POST.get('niter'))
    met=int(request.POST.get('method'))
    if(met==0):
        method='jacobi'
    elif(met==1):
        method='gaussSeid'
    elif(met==2):
        method='sor'
    else:
        messages.error(request,"Estas ingresando incorrectamente a un metodo matricial")
        return redirect('selectionPage')
    # métodos:
    # - 0 -> jacobi
    # - 1 -> gauss-seidel
    # - 2 -> SOR
    w=0.5
    eng.code_MatJacobiSeidSor(tol,typeTol,niter,met,w) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
    #leemos el csv
    csv_file = open('data_iterativos.csv', 'r')
    data = csv_file.readlines()
    columnNames = [("n",""),("Error","")]
    for i in range(1,n+1):
        columnNames.append(("X",str(i)))
    table = []
    #creamos tabla
    for i in range(1, len(data)):
        row = data[i].split(',')
        row[len(row)-1] = row[len(row)-1].replace('\n','')
        table.append(row)
    #creamos solución
    ans=[]
    if(float(table[len(table)-1][1])<=tol):
        for i in table[len(table)-1][2:]:
            ans.append(i)
    else:
        ans.append("No logró converger el método")
    print(ans)
    return render(request, 'calculatorApp/cap2-showAns.html',context={
        'n':n,
        'ans':ans,
        'method':method,
        'tablaIter':table,
        'title':columnNames
    })

@csrf_exempt
def newton1(request):
    if (request.method == 'POST'):
        #Arguments we need to do the function
        x0 = request.POST.get('x0')   #Be careful to put all these data in float type!
        tol = request.POST.get('tolerancia')
        typeTol = request.POST.get('tipoError')
        niter = request.POST.get('niter')
        fun = request.POST.get('funcion') #read the function given
        x0 = x0.strip().replace('−', '-')
        eng.code_RaicesMultiples(float(x0),float(tol),float(typeTol),float(niter),fun) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
        csv_file = open('data_RaicesMultiples.csv', 'r')
        data = csv_file.readlines()
        columnNames = data[0].split(',')
        columnNames[len(columnNames)-1] = columnNames[len(columnNames)-1].replace('\n','')
        table = []
        for i in range(1, len(data)):
            row = data[i].split(',')
            row[len(row)-1] = row[len(row)-1].replace('\n','')
            table.append(row)
        print(table)
        if (columnNames[0] == 'Derivada de df(x0) es igual a 0, maximo o minimo local'):
            sol = 'Derivada de df('+table[0][0]+') es igual a 0, x0 es un maximo o minimo local'
        elif(columnNames[0] == 'MaximaRaiz'):
            sol = 'Cantidad de derivadas en 0 ha pasado el límite definido: ' + table[0][0]
        elif(columnNames[0] == 'Fracaso en iteraciones'):
            sol = 'Fracaso en ' + table[0][0] + ' iteraciones'
        else:
            sol = "solución es: " + table[len(table)-1][1]+ " con "+table[len(table)-1][0] + " iteraciones"
        return render(request, 'calculatorApp/newton1.html',context={'tablaIter':table,'title':columnNames,'sol':sol})
    
    return render(request,'calculatorApp/newton1.html',context={})

# -----------------------------------------Capítulo 3--------------------------------------------------------
@csrf_exempt
def splineLineal(request):
    if(request.method=='POST'):
        #leemos x
        x=request.POST.get('x')
        x=x.replace(' ','')
        #generamos x
        xFile=open("pointsX.txt",'w')
        xFile.write(x)
        xFile.close()
        #leemos y
        y=request.POST.get('y')
        y=y.replace(' ','')
        print(x)
        print(y)
        #generamos y
        yFile=open("pointsY.txt",'w')
        yFile.write(y)
        yFile.close()

        #corremos matlab
        eng.Spline(1)
        
        #leemos los datos del polinomio
        csv_file = open('data_Spline.csv', 'r')
        data = csv_file.readlines()
        columnNames = data[0].split(',')
        columnNames[len(columnNames)-1] = columnNames[len(columnNames)-1].replace('\n','')
        table = []
        for i in range(1, len(data)):
            row = data[i].split(',')
            row[len(row)-1] = row[len(row)-1].replace('\n','')
            table.append(row)

        print(table)
        return render(request, 'calculatorApp/splineLineal.html',context={'tablaIter':table,'title':columnNames})
        # return render(request, 'calculatorApp/splineCubico.html',context={'pol':ctxtPol})
    
    else:
        return render(request, 'calculatorApp/splineLineal.html',context={})

@csrf_exempt
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

def splineLineal(request):
    return render(request,'calculatorApp/splineLineal.html',context={})

def splineCubico(request):
    if(request.method=='POST'):
        #leemos x
        x=request.POST.get('x')
        x=x.replace(' ','')
        #generamos x
        xFile=open("pointsX.txt",'w')
        xFile.write(x)
        xFile.close()
        #leemos y
        y=request.POST.get('y')
        y=y.replace(' ','')
        print(x)
        print(y)
        #generamos y
        yFile=open("pointsY.txt",'w')
        yFile.write(y)
        yFile.close()

        #corremos matlab
        eng.Spline(3)
        
        #leemos los datos del polinomio
        csv_file = open('data_Spline.csv', 'r')
        data = csv_file.readlines()
        columnNames = data[0].split(',')
        columnNames[len(columnNames)-1] = columnNames[len(columnNames)-1].replace('\n','')
        table = []
        for i in range(1, len(data)):
            row = data[i].split(',')
            row[len(row)-1] = row[len(row)-1].replace('\n','')
            table.append(row)

        print(table)
        return render(request, 'calculatorApp/splineCubico.html',context={'tablaIter':table,'title':columnNames})
        # return render(request, 'calculatorApp/splineCubico.html',context={'pol':ctxtPol})
    
    else:
        return render(request, 'calculatorApp/splineCubico.html',context={})


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
        for i in range(len(x)):
            x[i] = float(x[i])
            y[i] = float(y[i])
        response_data = {
            'points': "received",
        }
        eng.Spline(x,y,d) #call the function in matlab, be careful because the matlab file has to be in the same address of this code
        csv_file = open('data_Spline.csv', 'r')
        data = csv_file.readlines()
        columnNames = data[0].split(',')
        columnNames[len(columnNames)-1] = columnNames[len(columnNames)-1].replace('\n','')
        table = []
        for i in range(1, len(data)):
            row = data[i].split(',')
            row[len(row)-1] = row[len(row)-1].replace('\n','')
            table.append(row)
        sol = 1
        # return render(request, 'calculatorApp/splineCubico.html',context={'tablaIter':table,'title':columnNames,'sol':sol})
        # return  JsonResponse(response_data,safe = False)
    else:
        return JsonResponse({'error': 'Invalid request method'})

def newtonInter(request):
    if(request.method=='POST'):
        #leemos x
        x=request.POST.get('x')
        x=x.replace(' ','')
        #generamos x
        xFile=open("pointsX.txt",'w')
        xFile.write(x)
        xFile.close()
        #leemos y
        y=request.POST.get('y')
        y=y.replace(' ','')
        #generamos y
        yFile=open("pointsY.txt",'w')
        yFile.write(y)
        yFile.close()

        #corremos matlab
        eng.code_NewtonFull()
        #leemos los datos del polinomio
        csv_file = open('data_newtonInter.csv', 'r')
        data = csv_file.readlines()
        print(data)
        data=data[1].split(',')
        data[len(data)-1]=data[len(data)-1].replace("\n",'')
        #hacemos el str del polinomio
        strPol=''
        ctxtPol=[]
        length=len(data)
        for i in range(len(data)):
            #(coef,exp)
            ctxtPol.append((data[i],str(length-1-i)))
            if(i==length-1):
                strPol+=data[i]+"*xpol.^"+str(length-1-i)
            else:
                strPol+=data[i]+"*xpol.^"+str(length-1-i)+"+"

        #generamos pol
        polFile=open("polNI.txt",'w')
        text=""
        for t in data:
            text+=t+','
        polFile.write(text)
        polFile.close()

        eng.code_graficaNewton(strPol)
        print(ctxtPol)
        return render(request, 'calculatorApp/newtonInter.html',context={'pol':ctxtPol})
    
    else:
        return render(request, 'calculatorApp/newtonInter.html',context={})
    
def moveData(image_name, csv_name):
    file_path = os.path.join(BASE_DIR, image_name)
    destination_path = os.path.join(BASE_DIR, 'calculatorApp', 'static', 'images', image_name)
    os.rename(file_path, destination_path)

    file_path = os.path.join(BASE_DIR, csv_name)
    destination_path = os.path.join(BASE_DIR, 'calculatorApp', 'static', 'csv', csv_name)
    os.rename(file_path, destination_path)

def getInfoTable(file_name, tol, niter):
    file_path = os.path.join(BASE_DIR, 'calculatorApp', 'static', 'csv', file_name)
    csv_file = open(file_path, 'r')
    data = csv_file.readlines()
    columnNames = data[0].split(',')
    columnNames[len(columnNames)-1] = columnNames[len(columnNames)-1].replace('\n','')

    table = []
    for i in range(1, len(data)):
        row = data[i].split(',')
        row[len(row)-1] = row[len(row)-1].replace('\n','')
        table.append(row)

    try:
        row = table[len(table)-1]
        if(float(row[len(row)-1]) <= float(tol)):
            sol = row[1]
            sol = f"La solución obtenida es: {sol}"
        else:
            sol=f"No se llegó a la respuesta esperada con {niter} iteraciones"
    except(ValueError):
        sol = "Recuerda que la solución debe estar dentro del intervalo ingresado"
    return columnNames, table, sol
