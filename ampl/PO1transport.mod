param n; # número de variáveis
param d; # número de demandas
param s; # número de ofertas

set J = {1..n}; # conjunto de variáveis
set I = {1..d}; # conjunto de demandas
set K = {1..s}; # conjunto de ofertas

param costs {J}; # custo de cada variável
param d_coef {I, J}; # coeficientes de demanda (binário)
param d_threshold {I}; # limite de demanda
param s_coef {K, J}; # coeficientes de oferta (binário)
param s_threshold {K}; # limite de oferta

var X {J} >= 0; # variáveis de decisão

minimize Transport_Cost: sum {j in J} costs[j] * X[j];

subject to Demands {i in I}: # restrição de  demanda
    sum {j in J} d_coef[i, j]* X[j] >= d_threshold[i];

subject to Offers {k in K}: # restrição de oferta
    sum {j in J} s_coef[k, j]* X[j] <= s_threshold[k];