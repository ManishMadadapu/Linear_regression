from numpy import *

t_0 = 0 #Parameter 1
t_1 = 0 #Parameter 2
learning_rate = 0.0001
iterations = 1000
data = array(genfromtxt('data.csv',delimiter = ',')) # data coverted into the form of an array
temp_0 = 0 # temporary prameter
temp_1 = 0# temporary prameter
m = len(data)

# gradient descent
for i in range(iterations):
    for i in range(m):
                x = data[i,0]
                y = data[i,1]
                temp_0 -= learning_rate*(1/m*((t_0 + t_1*x)-y) )
                temp_1 -= learning_rate*((1/m*((t_0 + t_1*x)-y) )*x)
    t_0 = temp_0
    t_1 = temp_1
    
    
   #prints the final result of the gradient descent
print("t_0:", t_0)
print("t_1:",t_1)
