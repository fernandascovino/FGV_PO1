set items;

param weights {items};
param values {items};

var y {i in items} binary;
var z binary; # variável indicadora de weights > 20

# Queremos maximizar o valor total dos items na mochila podendo pagar, a cada kg acima de 20, mais $15
maximize Total_value:
    sum {i in items} values[i] * y[i] - 15 * (sum {i in items} weights[i] * y[i] - 20) * z;

subject to Exceded_weight: # se weights > 20 ==> z = 1
    (sum {i in items} weights[i] * y[i]) <= 20 + z * sum {i in items} weights[i];

subject to Exceded_weight_0: # se weights <= 20 ==> z = 0
    (21 - sum {i in items} weights[i] * y[i]) * z <= 0;