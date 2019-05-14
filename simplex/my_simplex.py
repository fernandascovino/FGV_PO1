import numpy as np

def my_simplex_step1(A, b, c):
    """
    Realiza um passo simplex, dado um PL na forma padrao.

    Parameters
    ----------
    A : np.matrix
        Matriz das restricoes do PL
    b : np.matrix
        Solucao basica do PL
    c : np.matrix
        ???
    
    Returns
    -------
    x1 : np.matrix
        
    t : int
        Tamanho do passo
    k : int
        Coluna da maior direcao
    """
    
    var_basicas = c[c==0]
    var_nao_basicas = c[c>0]
    
    # Encontrar a direcao para iterar (indice da coluna em A que vamos usar para direcoo)
    k = np.argmax(c)
    print('k: {}'.format(k))
    
    # Encontrar tamanho do passo
    rows = b.shape[0]
    print(rows)
    t = 0

    for i in range(rows):
        print('No idx {}: {}'.format(i, A[k, i]))
        next = b[i] / A[k, i]
        if next < t and next > 0:
            t = next

    # Dar o passo escolhido
    x_aux = b
    x_aux = x_aux - t*A[:, k]
    
    x1 = np.zeros(var_nao_basicas.shape[1], 1)
    x1[k, 1] = t
    x1 = [x1, x_aux]
    
    #x_aux = b - 0* A(:,1) - t*A(:,2)
    #x1 = [0; t]
    #x1 = [x1 ; x_aux]

A = np.matrix([[1,1,1,0,0], [2,1,0,1,0], [-1,1,0,0,1]])
b = np.matrix([0,0,6,10,4]).reshape(5,1)
c = np.matrix([2,3,0,0,0])

my_simplex_step1(A, b, c)



