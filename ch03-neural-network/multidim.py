import numpy as np

A = np.array([1,2,3,4])
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])

B = np.array([[1,2],[3,4],[5,4]])
print(B)
print(np.ndim(B))
print(B.shape)
print(B.shape[0])

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = np.dot(A, B)
print(C)

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,2],[3,4],[5,6]])
C = np.dot(A, B)
print(C)

A = np.array([[1,2],[3,4],[5,6]])
B = np.array([7,8])
C = np.dot(A, B)
print(C)

A = np.array([[1,2],[3,4],[5,6]])
B = np.array([[7],[8]])
C = np.dot(A, B)
print(C)
