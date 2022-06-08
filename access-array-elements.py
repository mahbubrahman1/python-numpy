# The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc. like list
import numpy as np

# arr = np.array([6, 5, 3, 8])
# print(arr[2])
# print(arr[0])

# add = arr[0] + arr[2]
# print(add)

# ? Access 2-D Arrays
# arr = np.array([[5, 6, 3], [6, 7, 3]])
# print(arr[0, 1])
# print(arr[0][1])
# print(arr[1, 0])

# ? Access 3-D Arrays
# myArray = [[[6, 7, 4], [8, 9, 7]], [[4, 5, 2], [4, 7, 9]]]
# npArray = np.array(myArray)
# print(npArray[0, 1, 2])

# ? Negative Indexing
arr = np.array([[2, 5, 6], [7, 3, 1]])
print(arr[1, -1])
print(arr[1, -2])
