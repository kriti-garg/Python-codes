import numpy as np
from matplotlib import pyplot as plt

iteration = 100
x = -2
neta = 0.1
#x_old = x;
# arr = list(range(100))
arr = [0] * iteration
loss_value = [0] * iteration
arr[0] = x
loss_value[0] = 4

for i in range(1,iteration):
    x = x - neta * (2*x)
    arr[i] = x
    y = x**2
    loss_value[i] = y
    
for i in range(iteration):
    print(arr[i])

for i in range(iteration):
    print(loss_value[i])

plt.plot(range(iteration), loss_value)
plt.show()