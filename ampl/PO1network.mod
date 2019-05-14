# dic = {x12 = X1, x13 = X2, x23 = X3, x24 = X4, x34 = X5, x35 = X6, x45 = X7, x53 = X8}

param n; # número de variáveis (arestas)
param m; # número de nós

set J = {1..n}; # conjunto de arestas
set I = {1..m}; # conjunto de nós

param cost {J}; # custo de cada aresta
param capac {J}; # capacidade de cada aresta
param inc {I, J}; # matriz de incidência
param total_flow {I}; # fluxo total de cada nó (qtde ao final) 

var X {J} >= 0; # variáveis de decisão (fluxo nas arestas)

minimize Total_cost: sum {j in J} cost[j] * X[j];

# fluxo total de cada nó (qtde ao final)
subject to Total_flow {i in I}:
    sum {j in J} inc[i, j] * X[j] = total_flow[i];

# fluxo máximo de cada aresta
subject to Max_flow {j in J}:
    X[j] <= capac[j];

# conexões da rede (entrada = saída)
subject to Flow_1: X[1] + X[2] = 20;
subject to Flow_2: X[1] = X[3] + X[4];
subject to Flow_3: X[2] + X[3] + X[8] = X[5] + X[6];
subject to Flow_4: X[4] + X[5] = X[7] + 5;
subject to Flow_5: X[7] = X[8] + 15;
