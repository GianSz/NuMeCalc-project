function pol = code_vandermonde()

    A = readmatrix('matrix-A_vandermonde.txt')
    b = readmatrix('matrix-b_vandermonde.txt')
    pol = A\b;
    table = array2table(pol);
    writetable(table, 'polinomio_vandermonde.csv');

end