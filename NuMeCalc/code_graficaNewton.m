function [grafica] = code_graficaNewton(fun)

    x = readmatrix('pointsX.txt');
    y = readmatrix('pointsY.txt');
    pol= readmatrix('polNI.txt');
    xpol=x(1):0.001:x(end);

    %espacio para el polinomio
    mypol=evalin(symengine,fun);
    ypol=eval(subs(mypol,xpol));
    %ypol=pol(1)*xpol.^2+pol(2)*xpol.^1+pol(3);

    %ymin=min(ypol);
    fig=figure;
    plot(x,y,'r*')
    hold on
    grid on
    plot(xpol,ypol,'g')
    print(fig,'grafica_newtonInter','-dpng')
    grafica = "se logra graficar";
end