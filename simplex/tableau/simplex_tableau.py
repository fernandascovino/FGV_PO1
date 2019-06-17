import numpy as np

def SimplexTableau(A, b, c, B, w=0, max_counter=100):
    """
    Solves LP in the format:  max{z = cx + w : Ax = b, x >= 0}
    
    Return
    ------
    T : np.array
        Tableau with the solution. 
        To separate the solution, just pick the columns of T that forms a identity and do a dot product with b.
    """
    
    T = np.concatenate((np.zeros(A.shape[0]).reshape(A.shape[0],1), A, b), axis=1)
    T = np.concatenate((np.array([1] + list(-c.T[0]) + [0]).reshape(1, c.shape[0]+2), T), axis=0)
    
    counter = 0

    while np.any(T[0,:] < 0) and (counter < max_counter):

        print('>>> Iteração {}:'.format(counter))
        j = np.where(T[0,1:-1] < 0)[0][0] # primeiro elemento em quem -c > 0 (exceto primeira e última colunas)
        j = j+1 # pulamos a primeira coluna

        razao = T[1:, -1]/T[1:, j] # divide os valores de b pela coluna (máximo de aumento da variável da coluna k)
        razao = np.where(razao < 0, np.nan_to_num(np.inf), razao) # substitui valores negativo por +inf

        i = np.argmin(razao) # obtem o índice do menor valor (menor dentre os máximos para a variável da coluna k)
        i = i+1 # pulamos a primeira linha

        T[i,:] = T[i,:]/T[i, j] # dividindo a linha pelo valor escolhido

        for l in range(T.shape[0]):

            if l != i:
                m = T[l, j]/T[i,j] # fator multiplicativo para zerar o elemento
                T[l,:] = T[l,:] - m*T[i,:]

            else:
                T[i,j] = T[i,j]

        counter +=1
        print('j: {}'.format(j))
        print('i: {}'.format(i))
        print('T: {}\n'.format(T.round(2)))
      
    return T

if __name__ == '__main__':
    print('here!')