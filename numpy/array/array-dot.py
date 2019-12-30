import numpy as np



a = np.array([[1, 2, 3]])
b = np.array([[4], [5], [6]])

c = np.dot(a, b)

print (a)
print (a.shape)
print (b)
print (b.shape)
print (c)
print (c.shape)

print ('-------------')

a = np.array([[1], [2], [3]])
b = np.array([[4, 5, 6]])

c = np.dot(a, b)

print (a)
print (a.shape)
print (b)
print (b.shape)
print (c)
print (c.shape)

print ('-------------')

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

c = np.dot(a, b)

print (a)
print (a.shape)
print (b)
print (b.shape)
print (c)
print (c.shape)
