param n; # número de variáveis
param m; # número de ofertas (vacas)

set J = {1..n}; # conjunto de variáveis
set C = {1..m}; # conjunto de ofertas

param profit {J}; # lucro unitário dos tipos de leite
param volum {J}; # volume unitário dos tipos de leite
param milk_fat_req {J}; # porcentagem de gordura por unidade de leite
param cow_litres {C}; # volume total de leite das ofertas
param cow_milk_fat {C}; # porcentagem de gordura no leite das ofertas

var X {J} integer >= 0; # variáveis de decisão (unidades a serem produzidas de cada tipo de leite)
var m_1 >= 0; # m_1 = % gordura da unidade de Skimmed milk
var w >= 0; # variável X[1]*m1

maximize Total_profit: sum {j in J} profit[j] * X[j];

subject to Total_milk_fat: 
    (sum {j in 2..n} X[j] * milk_fat_req[j] * volum[j] + w * volum[1]) / 100 <= sum {c in C} cow_milk_fat[c] * cow_litres[c] / 100;

subject to McCormick_envelope_upper1:
    w <= 0.1 * X[1];

subject to McCormick_envelope_upper2:
    w <= 375 * m_1; 

subject to McCormick_envelope_lower:
    w >= (375 * m_1 + 0.1 * X[1] - 37.5);

# removendo gordura do total de litros de leite
subject to Total_fat_free:
    sum {j in 2..n} (X[j] * volum[j] - X[j] * volum[j] * milk_fat_req[j]/100) + (X[1] * volum[1] - w * volum[1]/100) <= sum {c in C} cow_litres[c] * (1 - cow_milk_fat[c]/100);