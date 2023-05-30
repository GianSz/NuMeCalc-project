function [out] = code_vandermonde()

    x = readmatrix('pointsX.txt')';
    y = readmatrix('pointsY.txt')';
    V = vander(x);
    
    pol = V\y;
    pol = pol';

    out = array2table(pol);
    writetable(out, 'data_vandermonde.csv');

end