import numpy as np
from numpy.linalg import inv

def find_basis(A, c, b):
    """
    Gera uma base para o problema, determinando se o problema é factível.

    Return
    ------
    B : np.array
        Base para o PL.
    x : np.array
        Solução básica associada a B.
    """

    print("Buscando uma base...")

    # Criamos i novas variáveis
    i = A.shape[0]
    print('Expansão da matriz A:')
    A_exp = np.append(A, np.identity(i), axis=1)
    print(A_exp)

    print('Atualizando c e criando a base inicial:')
    c = np.zeros((A_exp.shape[1], 1))
    c[-i:] = -1
    B = np.where(c == -1)[0]
    print('c: \n', c)
    print('B: ', B)

    print('Solução inicial:')
    #pinv = np.linalg.pinv(A_exp)
    #x = np.dot(pinv, b)
    x = np.zeros(A_exp.shape[1])
    x[B] = np.dot(A_exp[:, B], b).reshape(B.shape[0])
    print(x)

    # Calculando simplex para o problema "artificial"
    s = Simplex(A_exp, c, b, B=B, maximum=False)
    x = s.fase_2()

    # Checando solução factível: variáveis novas devem estar zeradas!
    if np.all(x[-i:] == 0):
        B = np.where(x[:-i] != 0)[0]
        
        x = np.zeros(A.shape[1])
        x[B] = np.dot(A_exp[:, B], b).reshape(B.shape[0])
        x = x.reshape(x.shape[0], 1)
        
        print(">> Base encontrada: \nB = \n{}".format(B))
        print(">> Solução básica: \nx = \n{}".format(x))
        return B

    else:
        print("Problema não é factível :(")


class Simplex:

    """
    Instancia o metodo Simplex.

    Parameters
    ----------
    A : np.matrix
        Matriz de restricoes do PL
    c : np.array
        Vetor de custos do PL.
    b : np.array
        Vetor de resposta do PL.
    B : np.array, optional
        Base do PL (pode ser encontrada na fase 1).
    maximum : bool
        Define problema de maximização (True) ou minimização (False). Defautl True.
    w : int
        Custo independente do PL.
    steps : int, optional
        Número máximo de iterações. Default 100.

    Return
    ------
    x : np.array
        Solucao otima do PL (nx1).
    """
    def __init__(self, A, c, b, B=np.nan, maximum=True, w=0, steps=500):

        self.A = A
        self.c = c
        self.b = b
        self.w = w
        self.steps = steps
        
        if type(B) == np.ndarray:
            self.B = B
            
        if maximum:
            self.operator = max
        else:
            self.operator = min
            
    def canonical_form(self):
        """
        Passa o PL para a forma canônica: (i) A_B deve ser identidade, (ii) c_B = 0
        """
        
        if not np.all(self.c[self.B] != 0) or not np.all(self.A[:, self.B] != np.identity(len(self.B))):
            
            A_Binv = np.linalg.inv(self.A[:, self.B])
            self.y = A_Binv.T.dot(self.c[self.B])
            self.c = self.c.T - self.y.T.dot(self.A).ravel()
            self.c = self.c.T
            self.w = self.w + np.dot(self.y.T, self.b)
            
            self.A = A_Binv.dot(self.A)
            self.b = A_Binv.dot(self.b)
            
            self.x = np.zeros(self.A.shape[1])
            self.x[self.B] = np.dot(self.A[:,self.B],self.b).reshape(self.B.shape[0])
            
            print('A: \n', self.A.round(2))
            print('b: \n', self.b.round(2))
            print('c: \n', self.c.round(2))
            print('w: \n', self.w)
            print(">> Problema canonizado! x: ", self.x)
            
        else:
            print(">> Problema ja na forma canonica! x: ", self.x)
    
    def step(self):
        
        x = np.zeros(self.A.shape[1])
        x[self.B] = np.linalg.solve(self.A[:, self.B], self.b).T
        
        # Encontrar tamanho do passo
        rows = self.b.shape[0]
        
        t_set = np.array([self.b[i]/self.A[i, self.k] for i in range(rows)])
        #t = t_set[t_set > 0] # t > 0
        t_set = t_set[t_set > 0] # t > 0
        print('t: {}'.format(t_set))
        
        if self.operator:
            t = min(t_set) # problema de maximizacao
        else:
            t = max(t_set) # problema de minimizacao
            
        self.r = np.where(t_set == t)[0][0]
        print('r: {}'.format(self.r))

        # Dar o passo escolhido: x_B = b - t*Ak
        x_B = self.b - t*self.A[:, self.k].reshape(self.A.shape[0], 1)
        x_B = np.array(x_B.tolist())
        
        self.x = np.zeros((self.c.shape[0], 1))
        self.x[self.k] = t
        
        self.x[self.B] = x_B
        print('>> x: \n{}'.format(self.x))

    def fase_1(self):
        
        print('\n\nFASE 1:')
        self.B = find_basis(self.A,  self.c, self.b)
        
    def fase_2(self):
        
        print('\n\nFASE II:')
        self.N = list(set(range(self.A.shape[1])) - set(self.B))

        i = 0
        while i < self.steps:
            print("\n>>> Iteração {}:".format(i))
            print("\n1. Reescrevendo o PL na forma canonica para a base B...\n")
            self.canonical_form()
            
            print("\n2. Teste de otimalidade (c_N <= 0):")
            if np.all(self.c[self.N] <= 0):
                print(">>> Processo terminado!")
                return self.x
            print("Não passou no teste...\n")
            print(">> c_N: \n{}".format(self.c[self.N]))

            print("\n3. Seleciona k em N tal que c[k] > 0...")
            #print(np.where(self.c > 0))
            self.k = np.where(self.c > 0.0001)[0][0] # primeiro valor não nulo
            print(">> k: {}".format(self.k))
            
            print("\n4. Teste de unboundness (A[:,k] <= 0):")
            if np.all(self.A[:, self.k] <= 0):
                (">>> Processo terminado! O problema é ilimitado :(")
                return
            print("Não passou no teste...\n")
            print(">> A[:,k]: \n{}".format(self.A[:, self.k].round(2)))
            
            print("\n5. Passo Simplex...")
            self.step()

            print("\n6. Atualizando a base...")
            print(self.B)
            self.B = np.append(self.B, self.k)
            print('Adicionando o elemento k (k = {}):'.format(self.k))
            print(self.B)
            self.B = np.delete(self.B, self.r)
            print('Removendo o r-ésimo elemento (r = {}):'.format(self.r))
            print(self.B)
            
            self.N = list(set(range(self.A.shape[1])) - set(self.B))
            print(">> B: \n{}".format(self.B))
            
            i += 1

        print("Processo terminado!")
        return self.x
    
if __name__ == '__main__':
    
    print('Here!')