a = list(range(5,11))
print(a)

arr = list(range(1,5))
print(arr)

print(type(arr[0]))


import numpy as np
a = np.array(arr)
print(a)
print(a[-1])

print(a.size)
print(a.shape)
print(a)

a = a.reshape(4,1)
print(a.shape)
print(a)

a = a.reshape(2,2)
print(a.shape)
print(a)

a = a.reshape(1,4)
print(a.shape)
print(a)

print(type(a))


are = list(range(1,7))
p = np.array(are)
print(p)
# p = p.reshape(6,1)
p = np.reshape(p, (6,1))
print(p)
p = p.reshape(2,3)
print(p)
print(p.ndim)
print(np.ndim(p))
# [[1 2 3]
#  [4 5 6]]

p = p.reshape(1,6)
print(p)
# [[1 2 3 4 5 6]]

p = p.reshape(1,2,3)
print(p)
print(p.shape)
print(np.shape(p))
print(p.ndim)
# [[[1 2 3] [4 5 6]]]

pib = [[1,2,3],[4,5,6]]
pib = np.array(pib)
print(pib)
pi2 = [    [1,2,3],[4,5,6],[7,8,9]    ]
pi2 = np.array(pi2)
print(pi2)
print(np.ndim(pi2))

pi3 = [ [[1,2],[3,4]], [[5,6], [7,8]], [[1,2],[3,4]],  [[5,6], [7,8]] ]
pi3 = np.array(pi3)
print(pi3)
print(np.ndim(pi3))
print(np.shape(pi3))

pi4 = [[[[1,2],[3,4]], [[5,6],[7,8]]]]
pi4 = np.array(pi4)
print(pi4)
print(np.ndim(pi4))
print(np.shape(pi4))
# (1,2,2,2)

# print(pib)
ar1 = np.array([1,2,3,4], dtype=np.float64)
print(ar1)
print(ar1.dtype)
print(ar1.shape)

