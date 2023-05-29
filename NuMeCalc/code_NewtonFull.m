function [out] = code_NewtonFull()

    x = readmatrix('pointsX.txt')
    y = readmatrix('pointsY.txt')

    %number of points
    n=length(x);

    Tabla=zeros(n,n+1);
    Tabla(:,1)=x;
    Tabla(:,2)=y;
    for j=3:n+1
        for i=j-1:n
            Tabla(i,j)=(Tabla(i,j-1)-Tabla(i-1,j-1))/(Tabla(i,1)-Tabla(i-j+2,1));
        end
    end

    %la convertimos en los coeficientes
    coef= diag(Tabla,+1);

    pol=1;
    acum=pol;
    pol=coef(1)*acum;
    for i=1:n-1
        pol=[0 pol];
        acum=conv(acum,[1 -x(i)]);
        pol=pol+coef(i+1)*acum;
    end
    out=array2table(pol);
    writetable(out,'data_newtonInter.csv')
end