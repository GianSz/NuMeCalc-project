%MatJacobiSeid: Calcula la solución del sistema
%Ax=b con base en una condición inicial x0,mediante el método de Jacobi o
%de Gauss Seidel o SOR(Matricial), depende del método elegido, se elige 0 o 1 o 2 en met
%respectivamente

%tabla respuesta [iter error x1 x2 x3...xn]

function listTable = code_MatJacobiSeidSor(Tol,TypeTol,niter,met,w)
    x0=readmatrix('matrix-x0.txt');
    A=readmatrix('matrix-A.txt');
    b=readmatrix('matrix-b.txt');
    c=0;
    error=Tol+1;
    listTable=code_createTable(c,error,x0,[]);
    D=diag(diag(A));
    L=-tril(A,-1);
    U=-triu(A,+1);
    while error>Tol && c<niter
        if met==0
            T=inv(D)*(L+U);
            C=inv(D)*b;
            x1=T*x0+C;
        end
        if met==1
            T=inv(D-L)*(U);
            C=inv(D-L)*b;
            x1=T*x0+C;
        end
        if met==2
            T=inv(D-w*L)*((1-w)*D+w*U);
            C=w*inv(D-w*L)*b;
            x1=T*x0+C;
        end
        if TypeTol==0
            error=norm(x1-x0,'inf');
        else
            error=(norm(x1-x0,'inf'))/norm(x1,'inf');
        end
        x0=x1;
        c=c+1;
        listTable=code_createTable(c,error,x0,listTable);
    end
    listTable=array2table(listTable);
    writetable(listTable,'data_iterativos.csv')
    if error < Tol
        fprintf('es una aproximación de la solución del sistmea con una tolerancia= %f',Tol)
    else
        fprintf('Fracasó en %f iteraciones',niter) 
    end
end