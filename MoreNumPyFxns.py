import numpy as np
p = [[[[1,2],[3,4]],[[5,6],[7,8]]]]
p = np.array(p)
print(np.ndim(p))
print(np.size(p))
print(p.shape)
print(p)

print(np.array(p).size)

q = [[[1,2],[3,4],[5,6]]]


# q = [[[1,2],[3,4],[5,6]]]
print(q)
print(np.array(q).size)
print(np.array(q).shape)


r = [1,2,3]
print(r)
print(np.array(r).size)
print(np.array(r).shape)

o = [[1,2,3]]
print(o)
print(np.array(o).size)
print(np.array(o).shape)

l = [[[1,2],[3,4]],[[5,6],[7,8]]]
print(l)
print(np.array(l).size)
print(np.array(l).shape)

l = np.array(l)
print(l)
print(l.T)

o = np.array(o)
print(o)
print('hi')
print(o.T)
print(np.transpose(o))
print(o.transpose())


# Elementwise multiplication
print(o * 2)
print(l * 2)
print(o/2)
print(o+2)
print(l+2)
print(l ** 2)

print(l)
print(l>5)
l[l>5] = 9
print(l)
l[:] = 10
print(l)

# n X n identity matrix
t1 = np.eye(5)
print(t1)
print(t1.size)
print(t1.shape)

# 5 X 1 matrix
t2 = np.zeros((5,1))
print(t2)

t3 = np.zeros((4,5,3))
print(t3)

t2 = np.ones((5,1))*7
print(t2)

t4 = np.diag(t1)
print(t4)

t3 = np.random.random((5,5))
print(t3)
# print(t3[:,:4])
print(t3[:,2:3])
# print(t3[:,2:])

# Ways of accessing 2nd row
print(t3[1])
print(t3[1,:]) 

print(t3[1,3]) # element (2,4)

print(t3[1:5,:])
print(t3[1:5])

print(t3[:,1])
print(t3[:,1].shape)
print(t3[:,1:2])
print(t3[:,1:2].shape)

a = np.array([1,2,3])
print(a)
print(a.shape)
a = a.reshape(3,1)
print(a)
print(a.shape)