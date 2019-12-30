import numpy as np

arr = np.asarray([1, 2, 3])

print (arr)
print (arr.shape) #shape is represented as tuple

print ("-----")

arr = np.asarray([[1, 2, 3], [4, 5, 6]])

print (arr)
print (arr.shape) #shape is represented as tuple

print ("-----")

arr = np.zeros((2, 3))

print (arr)

print ("-----")

arr = np.ones((2, 3))

print (arr)

print ("-----")

arr = np.identity(4)

print (arr)

print ("-----")

arr = np.random.rand(2, 3)

print (arr)

print ("-----")

arr = np.random.randn(2, 3) # random as normal distribution

print (arr)

print ("-----")
