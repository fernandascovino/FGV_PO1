set items;

param weights {items};
param values {items};

var y {i in items} binary;

# Queremos maximizar o valor total dos items na mochila não excedendo o peso
maximize Total_value:
    sum {i in items} values[i] * y[i];

subject to Total_weight:
    sum {i in items} weights[i] * y[i] <= 20;