set tasks;
param duration {tasks};

var start {i in tasks} >= 0; # tempo de inicio de cada tarefa
var Y; # variável para linerizacao max-min

minimize Max_time: Y; # tempo total

# tempo total = incio + duracao da ultima tarefa (max)
subject to Max_time_const {i in tasks}:
    start[i] + duration[i] <= Y;

subject to const0:
    start['F'] >= start['B'] + duration['B'];

subject to const1:
    start['L'] >= start['B'] + duration['B'];

subject to const2:
    start['E'] >= start['F'] + duration['F'];

subject to const3:
    start['P'] >= start['F'] + duration['F'];

subject to const4:
    start['D'] >= start['E'] + duration['E'];

subject to const5:
    start['D'] >= start['P'] + duration['P'];