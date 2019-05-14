param n; # número de variáveis
param m; # número de ofertas (vacas)

set J = {1..n}; # conjunto de variáveis
set C = {1..m}; # conjunto de ofertas

param profit {J}; # lucro unitário dos tipos de leite
param volum {J}; # volume unitário dos tipos de leite
param milk_fat_req {J}; # porcentagem de gordura por unidade de leite
param cow_litres {C}; # volume total de leite das ofertas
param cow_milk_fat {C}; # porcentagem de gordura no leite das ofertas

var X {J} >= 0 integer; # variáveis de decisão (unidades a serem produzidas de cada tipo de leite)

maximize Total_profit: sum {j in J} profit[j] * X[j];

subject to Total_milk_fat: 
    sum {j in J} X[j] * milk_fat_req[j] * volum[j] / 100 <= sum {c in C} cow_milk_fat[c] * cow_litres[c] / 100;

subject to Total_fat_free:
    sum {j in J} X[j] * volum[j] * (1 - milk_fat_req[j]/100) <= sum {c in C} cow_litres[c] * (1 - cow_milk_fat[c]/100);