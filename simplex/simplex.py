import numpy as np
from numpy.linalg import inv

class LinearProgram():

    def __init__(self):
        self.restrictions = np.nan
        self.costs = np.nan
        self.independent_cost = 0
        self.result = np.nan

    def basis(self):

        print("\nCalculando uma base para o PL...")
        self.base = np.where(self.costs == 0)[0]
        
        if len(self.base) == self.restrictions.shape[0]:
            
            print("Base achada! B = {}\n".format(self.base))

class Simplex:

    """
    Instancia o metodo Simplex.

    Parameters
    ----------
    PL : class LinearProgram
        Problema linear definido pela classe LinearProgram

    Return
    ------
    x : np.array
        Solucao otima do PL (nx1).
    """
    def __init__(self, PL):

        self.A = PL.restrictions
        self.c = PL.costs
        self.b = PL.result
        self.w = PL.independent_cost
        self.B = PL.base
        self.N = list(set(range(self.A.shape[0])) - set(self.B))
    
    def canonical_form(self):

        # 1. A_B deve ser a matriz identidade
        # 2. c_B = 0
            
        self.y = self.A[:, B].T.inv().dot(self.c[B])

        self.c = self.c.T - self.y.T.dot(self.A)
        self.w = self.w + self.y.T.dot(self.b)
        self.A = self.A[:, B].inv().dot(self.A)
        print("Problema canonizado! Indo para (2)...")
    
    def step(self):
        
        var_basicas = self.c[self.c==0]
        var_nao_basicas = self.c[self.c>0]
        
        # Encontrar tamanho do passo
        rows = self.b.shape[0]
        #print(rows)

        t = 0
        aux = 1
        i = 0
        while aux >= t or aux <= 0:
            aux = self.b[i] / self.A[i, self.k]
            i += 1
        
        self.t = aux

        # Dar o passo escolhido
        x_aux = b - t*A[:, k]
        x = np.zeros(var_nao_basicas.shape[1], 1)
        x[k, 1] = t
        self.x = [x, x_aux]
    
    def calculate(self):

        print(">>> Iniciando Simplex!")
        print("1. Reescrevendo o PL na forma canonica para a base B...")
        if self.c[self.B].any() != 0 or (self.A[:, self.B] != np.identity(len(self.B))).any():
            self.canonical_form()
        else:
            print("Problema ja na forma canonica! Indo para (2)...")

        print("2. Teste de otimalidade: c_N <= 0...")
        while self.c[self.N].any() > 0:

            print("3. Seleciona k em N tal que c[k] > 0...")
            self.k = np.argmax(self.c)

            print("4. Teste de unboundness: A[:,k] <= 0 (coluna)...")
            if self.A[:, self.k].any() <= 0:
                ("Processo terminado!")
                return x
            
            print("5. Passo Simplex...")
            self.step()

            print("6. Atualizando a base...")
            self.B = set(self.B).add(self.k) - set([self.r])

        print("Processo terminado!")
        return x


# Formato do PL: max{z = c'x + w : Ax = b, x >= 0}
PL = LinearProgram()
PL.restrictions = np.matrix([[1,1,1,0,0], [2,1,0,1,0], [-1,1,0,0,1]])
PL.costs = np.array([2,3,0,0,0])
PL.result = np.array([0,0,6,10,4]).reshape(5,1)
PL.basis()

x = Simplex(PL)
x.calculate()