from numpy import *

t_0 = 0
t_1 = 0
learning_rate = 0.0001
iterations = 1000
txt = genfromtxt('data.csv',delimiter = ',')
data = array(txt)
temp_0 = 0 
temp_1 = 0
m = len(data)
for i in range(iterations):
    for i in range(m):
                x = data[i,0]
                y = data[i,1]
                temp_0 -= learning_rate*(1/m*((t_0 + t_1*x)-y) )
                temp_1 -= learning_rate*((1/m*((t_0 + t_1*x)-y) )*x)
    t_0 = temp_0
    t_1 = temp_1
print("t_0:", t_0)
print("t_1:",t_1)
