set inputs; # linha de inputs ('origens')
set states; # linha de outputs ('destinos')

param cost {inputs}; # custo dos barris/dia
param capacity {inputs}; # capacidade de barris/dia em cada linha de input
param demand {states}; # número de barris demandados/dia

var barels {i in inputs} >= 0 integer; # número de barris/dia em cada input
var x binary; # variável para adição do custo fixo do input Yukon (barels[0])

# Queremos otimizar o número de barris devem ser bombeados em cada linha de input
minimize Total_cost: 11000 * x + sum{i in inputs} barels[i] * cost[i];

subject to Total_demands {j in states}:
     sum {i in inputs: i <= j} barels[i] >= demand[j];

subject to Total_barels:
    sum {i in inputs} barels[i] = sum {j in states} demand[j];

subject to Total_capacities {i in inputs}:
    barels[i] <= capacity[i];

subject to Maximum_x: # se barels[0] >=1 ==> x = 1
    barels[0] <= capacity[0] * x;

subject to Minimum_x: # se barels[0] = 0 ==> x = 0
    barels[0] - x >= 0;