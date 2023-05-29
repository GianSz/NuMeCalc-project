function T = code_newtonRaph2(x0, tol , typeTol, niter, fun)
    f = evalin(symengine,fun);

    df = diff(f);
    ddf = diff(f, 2);
    
    i = 1;
    xm = x0;
    N(i) = 0;
    E(i) = tol+1;
    XM(i) = xm;

    fm = eval(subs(f, xm));
    dfm = eval(subs(df, xm));
    ddfm = eval(subs(ddf, xm)); 

    FM(i) = fm;
    DFM(i) = dfm;
    DDFM(i) = ddfm;
       
    den = dfm^2-fm*ddfm;
    
    niter = niter+1;

    while FM(i)~=0 && den~=0 && E(i)>tol && i<niter
        i = i+1;
        N(i) = i-1;
        xm_1 = xm;

        %We calculate the next xm
        xm = xm_1-(fm*dfm)/den;
        XM(i) = xm;

        %We evaluate the function, the derivative function and the second
        %derivate function in xm
        fm = eval(subs(f, xm));
        dfm = eval(subs(df, xm));
        ddfm = eval(subs(ddf, xm));
        
        %Assign those values to the corresponding array
        FM(i) = fm;
        DFM(i) = dfm;
        DDFM(i) = ddfm;

        %We calculate the denominator of the next xm
        den = dfm^2-fm*ddfm;
        if typeTol==0
            E(i) = abs(xm-xm_1);
        else
            E(i) = abs((xm-xm_1)/xm);
        end

    end

    if FM(i) == 0
        fprintf('%f es una raíz de la función\n', xm);
    elseif E(i)<tol
        fprintf('%f es una aproximación de una raíz de la función con una toleracia = %f\n', xm, E(i));
    elseif den==0
        fprintf('El denominador dió 0 en un punto\n');
    else
        fprintf('Fracasó en %f iteraciones\n', niter-1);
    end
    T = table(N', XM', FM', DFM', DDFM', E', VariableNames=["n","Xm","Fm","Dfm","Ddfm","Error"]);
    fig = figure('Visible', 'off');
    xplot=((xm-2):0.1:(xm+2));
    hold on
    yline(0);
    plot(xplot,eval(subs(f,xplot)));
    print(fig,'grafica_newtonRaph2','-dpng')
    hold off
    close(fig);
    writetable(T,'data_newtonRaph2.csv')
end