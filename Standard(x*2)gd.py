# J = x^2
# J = (x+1)(x-3)(x-5)(x-8)

import numpy as np
from matplotlib import pyplot as plt

iteration = 100
x = -2
neta = 0.1

x_old = x
J_values = []
xvar = []

for i in range(iteration):
    J_error = x_old**2
    Delta_J = 2 * x_old
    
    xvar.append(x_old)
    J_values.append(J_error)
    
    x_new = x_old - neta * Delta_J
    x_old = x_new

plt.plot(range(iteration), J_values)
plt.show()

figure;
plt.plot(range(iteration), xvar)
plt.show()