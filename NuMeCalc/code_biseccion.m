%Bisección:
%Se ingresa el valor inicial y final del intervalo (xi, xs)
%La tolerancia del error (Tol)
%El tipo de tolerancia (TypeTol) -> 0 para decimales correctos y 1 para
%cifras significativas
%El máximo número de iteraciones (niter) 

function T = code_biseccion(xi,xs,Tol,TypeTol,niter,fun)

    f=evalin(symengine,fun);
    fi=eval(subs(f,xi));
    fs=eval(subs(f,xs));
    
    %Revisamos si el inicio del intervalo ya es una raíz
    if fi==0
        E=0;
        fprintf('%f es raiz de f(x) \n',xi)
        N(1)= 1
        XM(1)=xi
        fm(1)=fi
        E(1)=0
        T = table(N', XM', fm', E', VariableNames=["n","Xn","Fm","Error"]);
        writetable(T,'data_biseccion.csv')
        
    
    %Revisamos si el final del intervalo ya es una raíz
    elseif fs==0
        E=0;
        fprintf('%f es raiz de f(x) \n',xs)
        N(1)= 1
        XM(1)=xs
        fm(1)=fs
        E(1)=0
        T = table(N', XM', fm', E', VariableNames=["n","Xn","Fm","Error"]);
        writetable(T,'data_biseccion.csv')
        
    
    %Revisamos que el intervalo si cumpla la condición
    elseif fs*fi<0
        %Inicializamos el contador en 0
        c=0;
        %Hallamos la primera Xm y lo guardamos en el arreglo de Xm
        xm=(xi+xs)/2;
        XM(c+1)=xm;
        %Hallamos f(Xm) y lo guardamos en el arreglo de fm
        fm(c+1)=eval(subs(f,xm));
        fe=fm(c+1);
        %Guardamos el primer error en el arreglo de errores
        E(c+1)=Tol+1;
        error=E(c+1);
        %Guardamos en un arreglo las iteraciones que llevamos
        N(c+1)=c+1;
        
        %Iteramos hasta que lleguemos a la solución o se llegue a la
        %tolerancia o al máximo de iteraciones
        while error>Tol && fe~=0 && c<niter
            %Revisamos cuál punta del intervalo debe cambiar, si a o b.
            if fi*fe<0
                xs=xm;
                fs=eval(subs(f,xm));

            else
                xi=xm;
                fi=eval(subs(f,xm));

            end
            
            xa=xm;
            xm=(xi+xs)/2;
            XM(c+2)=xm;
            fm(c+2)=eval(subs(f,xm));
            fe=fm(c+2);
            
            %Hallamos el error según lo que nos pidan (decimales correctos o cifras significativas)
            if TypeTol == 0
                E(c+2)=abs(xm-xa);

            else
                E(c+2)=abs((xm-xa)/xm);
            end

            error=E(c+2);
            N(c+2)=c+2;
            c=c+1;
        end

        if fe==0
           fprintf('%f es raiz de f(x) \n',xm)

        elseif error<Tol
           fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f \n',xm,Tol)

        else 
           fprintf('Fracasó en %f iteraciones \n',niter)

        end

        T = table(N', XM', fm', E', VariableNames=["n","Xn","Fm","Error"]);
        fig = figure;
        xplot=((xm-2):0.1:(xm+2));
        hold on
        yline(0);
        plot(xplot,eval(subs(f,xplot)));
        print(fig,'grafica_biseccion','-dpng')
        hold off
        writetable(T,'data_biseccion.csv')

    else
       fprintf('El intervalo es inadecuado') 
       N= ['-' '-']
       XM=['-' '-']
       fm=['-' '-']
       E=['-' '-']
       T = table(N', XM', fm', E', VariableNames=["n","Xn","Fm","Error"]);
       writetable(T,'data_biseccion.csv')

    end    
    
end