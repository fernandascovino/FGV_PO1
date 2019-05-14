set employee; # funcionários
var salary {i in employee} >= 0; # salário de cada funcionário

minimize Total_salaries: sum {i in employee} salary[i];

subject to const0:
    salary['Tom'] >= 20000;
    
subject to const1: 
    salary['Peter'] >= salary['Tom'] + 5000;

subject to const2: 
    salary['Nina'] >= salary['Tom'] + 5000;

subject to const3: 
    salary['Samir'] >= salary['Tom'] + 5000;

subject to const4: 
    salary['Gary'] >= salary['Tom'] + salary['Peter'];

subject to const5: 
    salary['Linda'] = salary['Gary'] + 200;

subject to const6: 
    salary['Nina'] + salary['Samir'] >= salary['Tom'] + salary['Peter'];

subject to const7: 
    salary['Bob'] >= salary['Peter'];

subject to const8: 
    salary['Bob'] >= salary['Samir'];

subject to const9: 
    salary['Bob'] + salary['Peter'] >= 60000;

subject to const10: 
    salary['Linda'] <= salary['Bob'] + salary['Tom'];