// Matriz de restrições
A = [1 1 1 0 0; 2 1 0 1 0; -1 1 0 0 1]

// Solução básica
x = [0,0,6,10,4]'

// B = uma possível base
B = [2,4,5]
N = [1,3]

A(:, B)*x(:, B) + A(:, N)*x(:, N)
A*x

