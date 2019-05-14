set racquets;
set manufacturers;

param profits {manufacturers, racquets}; # lucro unitário para cada raquete de cada fornecedor
param offers {manufacturers}; # máximo de raquetes a serem vendidas por cada fornecedor
param purchase {racquets}; # quantidade de raquetes desejadas

var racquets_order {manufacturers, racquets} >= 0 integer;

# Queremos maximizar o lucro obtido com as raquetes
maximize Total_profit:
    sum {i in manufacturers, j in racquets} profits[i, j] * racquets_order[i, j];

subject to Total_purchase {j in racquets}:
    sum {i in manufacturers} racquets_order[i, j] = purchase[j];

subject to Max_production {i in manufacturers}:
    sum {j in racquets} racquets_order[i, j] <= offers[i];
