import numpy as np
array_1 = np.array([42, 13, 1])
array_2 = np.array([[11,12,15], [18, 55, 78]])
print(array_1)
print(array_2[0,1])
print(np.zeros((4, 7)))
print(np.ones((4, 7)))
list_1 = [44, 56, 85]
print(list_1 * 3)
print(array_1 * 3)
array_3 = np.array([1, 5, 8])
print(array_1 * array_3)
print(np.arange(10))
print(np.arange(3, 15, 2))
print(np.arange(10).reshape((2,5)))
print(np.linspace(0, 5.5, 100)) 