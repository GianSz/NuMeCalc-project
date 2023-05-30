%Newton: 
%se ingresa el valor inicial (x0)
%la tolerancia del error (Tol) 
%el tipo de tolerancia (TypeTol): 0 decimales correctos - 1 cifras
%significativas
%el máximo número de iteraciones (niter) 
%Raíces múltiples

%function [n,xn,fm,dfm,E] = newton(x0,Tol,TypeTol,niter)

function T = code_RaicesMultiples(x0,Tol,TypeTol,niter,fun,m)
    %asignamos la f y le decimos que la tenga en términos de x
    syms x

    f=evalin(symengine,fun);
    %f=(21/2)*x * log(x+100)+x*x*log(x+100)+((9*(7*7))/16)*log(x+100);
    %hallamos la derivada de f
    df=diff(f);
    %contador en 0
    c=0;
    %agregamos al arreglo de funciones la f(x0) 
    fm(c+1) = eval(subs(f,x0));
    fe=fm(c+1);
    %agregamos al arreglo de derivadas la f'(x0)
    dfm(c+1) = eval(subs(df,x0));
    dfe=dfm(c+1);
    %agregamos el primer error al arreglo de ERRORES
    E(c+1)=Tol+1;
    error=E(c+1);
    %agregamos la primera x -> x0
    xn(c+1)=x0;
    if fe == 0
        E(1)=0
        T = table((0:1:c)', xn', fm',dfm', E', VariableNames=["n","x_n","f_m","df_m","E"])
    else
    %iteramos hallando las xn de Newton mientras no se llegue a la
    %tolerancia y que ni la función ni su derivada sea 0
    while error>Tol && fe~=0 && dfe~=0 && c<niter
        %parámetro m para las raíces múltiples
        xn(c+2)=x0-m*fe/dfe;
        fm(c+2)=eval(subs(f,xn(c+2)));
        fe=fm(c+2);
        dfm(c+2)=eval(subs(df,xn(c+2)));
        dfe=dfm(c+2);
        if TypeTol==0
            E(c+2)=abs(xn(c+2)-x0);
        else
            E(c+2)=abs((xn(c+2)-x0)/xn(c+2));
        end
        error=E(c+2);
        x0=xn(c+2);
        c=c+1;
    end
  
        if fe==0
           fprintf('%f es raiz de f(x) \n',x0)
           E(c+1)=0
           T = table((0:1:c)', xn', fm',dfm', E', VariableNames=["n","x_n","f_m","df_m","E"])
        elseif error<Tol
            fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f \n',x0,Tol)
            T = table((0:1:c)', xn', fm',dfm', E', VariableNames=["n","x_n","f_m","df_m","E"])
        elseif dfe==0
            fprintf('%f es una posible raiz múltiple de f(x) \nO simplemente un maximo o minimo local',x0)
            T = table(x0, VariableNames=["Derivada de df(x0) es igual a 0, maximo o minimo local"])
        else 
            fprintf('Fracasó en %f iteraciones \n',niter) 
            T = table(niter, VariableNames=["Fracaso en iteraciones"])
        end
    end
        fig = figure('Visible', 'off');
        xplot=((x0-2):0.1:(x0+2));
        hold on
        yline(0);
        plot(xplot,eval(subs(f,xplot)));
        print(fig,'grafica_newtonRaph1','-dpng')
        hold off
        close(fig);
        writetable(T,'data_newtonRaph1.csv') 
        
end