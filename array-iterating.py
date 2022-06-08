# Iterating means going through elements one by one. As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.


import numpy as np

# arr = np.array([3, 5, 7, 8])

# for i in arr:
#     print(i)


arr = np.array([[23, 56, 67], [43, 78, 33]])

# for i in arr:
#     print(i)

for i in arr:
    for j in i:
        print(j)
