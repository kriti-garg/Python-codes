from matplotlib import pyplot as plt
import numpy as np
iteration = 500
neta = 0.01
x = 5
arr = [0]*iteration
loss_fxn = [0]*iteration
for i in range(1,iteration):
    x = x - neta*(6*x)
    arr[i] = x
    y = x**2
    loss_fxn[i] = y
for i in range(iteration):
    print(arr[i])
for i in range(iteration):
    print(loss_fxn[i])
plt.plot(range(iteration),arr)
plt.show()