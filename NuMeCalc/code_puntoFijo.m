function T = code_puntoFijo(x0, tol ,typeTol, niter, fun, funG)
    f = evalin(symengine,fun);
    g = evalin(symengine, funG);
    
    fm = eval(subs(f, x0));
    if fm == 0
        s = x0;
        E = 0;
        fprintf('%f es una raíz de la función', x0);
    else
        i = 1;
        xm = x0;
        N(i) = 0;
        E(i) = tol+1;
        n(i) = xm;
        fm(i) = eval(subs(f, xm));
        
        niter = niter+1;
        while fm(i)~=0 && E(i)>tol && i<niter
            i = i+1;
            N(i) = i-1;
            xm_1 = xm;
            xm = eval(subs(g, xm));
            n(i) = xm;
            fm(i) = eval(subs(f, xm));
            
            if typeTol == 0
                E(i) = abs(xm-xm_1);
            else
                E(i) = abs((xm-xm_1)/xm);
            end
        end

        if fm(i) == 0
            fprintf('%f es una raíz de la función\n', xm);
        elseif E(i)<tol
            fprintf('%f es una aproximación de una raíz de la función con una toleracia = %f\n', xm, E(i));
        else
            fprintf('Fracasó en %f iteraciones', niter-1);
        end

    end
    T = table(N', n', fm', E', VariableNames=["n","Xm","Fm","Error"]);
    fig = figure;
    xplot=((xm-2):0.1:(xm+2));
    hold on
    yline(0);
    plot(xplot,eval(subs(f,xplot)));
    print(fig,'grafica_puntoFijo','-dpng')
    hold off
    writetable(T,'data_puntoFijo.csv')

end