function T = plotSpline(x, Tabla, d)
    n=length(x);
    xs=[];
    ys=[];
    for i=1:n-1
        xi=x(i):0.0001:x(i+1);
        if d==1
            xii=[xi ; ones(size(xi))];
        else
            xii=[xi.^3 ; xi.^2 ; xi ; ones(size(xi))];
        end
        fii=Tabla(i,:)*xii;
        xs = [xs xi];
        ys = [ys fii];
        
    end

    
    
    fig = figure('Visible', 'off');
    hold on
    plot(xs,ys,'lineWidth',2)
    xlabel("x");
    ylabel("y");
    print(fig,'grafica_Spline','-dpng')
    hold off
    close(fig);

end
