# J = x^2
# J = (x+1)(x-3)(x-5)(x-8)

import numpy as np
from matplotlib import pyplot as plt

iteration = 50
x = 5
neta = 0.03

x_old = x
J_values = []
xvar = []

for i in range(iteration):
    J_error = (x_old+1)*(x_old-3)*(x_old-5)*(x_old-8)
    Delta_J = (4*x_old*x_old*x_old)-(45*x_old*x_old)+(126*x_old)-41
    
    xvar.append(x_old)
    J_values.append(J_error)
    
    x_new = x_old - neta * Delta_J
    x_old = x_new


plt.plot(range(iteration), J_values)
plt.title('Error Function')
plt.show()

plt.figure()
plt.plot(range(iteration), xvar)
plt.title('X Values')
plt.show()