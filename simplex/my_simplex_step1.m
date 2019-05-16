function [x_1, t, k] = my_simplex_step1(A, b, c)
    
    var_basicas = c(c==0)
    var_nao_basicas = c(c>0)
    
    // Encontrar a direção para iterar (índice da coluna em A que vamos usar para direção)
    [val, k] = (max(c))
    
    // Encontrar tamanho do passo
    rows = size(b, 1)
    t = 0

    for i = 1:rows
       next = b(i) / A(i, k)
       if (next < t || next > 0)
           t = next
       end
    end
    
    // Dar o passo escolhido
    x_aux = b
    x_aux = x_aux - t*A(:, k)
    
    x_1 = zeros(size(var_nao_basicas, 2), 1)
    x_1(k, 1) = t
    x_1 = [x_1; x_aux]
    
    //x_aux = b - 0* A(:,1) - t*A(:,2)
    //x_1 = [0; t]
    //x_1 = [x_1 ; x_aux]
    
endfunction

A = [1 1 1 0 0; 2 1 0 1 0; -1 1 0 0 1]
b = [6,10,4]'
c = [2,3,0,0,0]
[x_1, t, k] = my_simplex_step1(A, b, c)



