import numpy as np

n = np.arange(0,20).reshape(4,5)
print(n)
print(n[1,2])
print("Row")
print(n[0:2])
print('Column')
print(n[:,-1])
print(n[:,-2])
print(n.ndim)
print(n.itemsize)
print(n.reshape(2,10))


