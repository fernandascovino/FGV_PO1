set packs;
set segments;
set info_packs;
set info_segments;

param packs_properties {packs, info_packs}; # propriedades dos tipos de engradados (peso, volume e valor)
param seg_properties {info_segments, segments}; # propriedades dos segmentos do avião (volume e capacidade de peso)
param packs_transport {packs}; # número de engradados disponíveis

# Matriz de variáveis: quantos engradados de cada tipo são carregados em cada segmento
var segment_cargo {packs, segments} >= 0 integer;

# Queremos maximizar o valor total dos engradados carregados
maximize Total_values:
    sum {i in packs} packs_properties[i, 'values'] * sum {j in segments} segment_cargo[i, j];
 
# Restrições de balanceamento de peso nos segmentos do avião
subject to Plane_distribution1:
    sum {i in packs} segment_cargo[i, 'Middle'] >= sum {i in packs} segment_cargo[i, 'Front'] +  sum {i in packs} segment_cargo[i, 'Back'];

subject to Plane_distribution2:
    sum {i in packs} segment_cargo[i, 'Middle'] <= 2 * (sum {i in packs} segment_cargo[i, 'Front'] +  sum {i in packs} segment_cargo[i, 'Back']);

# Máximo de packs disponíveis para transporte
subject to Maximum_packs {i in packs}:
    sum {j in segments} segment_cargo[i, j] <= packs_transport[i];

# Restrições de peso e volume total em cada segmento do avião
subject to Total_seg_weight {j in segments}:
    sum {i in packs} segment_cargo[i, j] * packs_properties[i, 'weights'] <= seg_properties['capacity', j];

subject to Total_seg_volum {j in segments}:
    sum {i in packs} segment_cargo[i, j] * packs_properties[i, 'volumes'] <= seg_properties['volume', j]
