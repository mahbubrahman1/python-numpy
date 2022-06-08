# You can search an array for a certain value, and return the indexes that get a match. To search an array, use the where() method.

import numpy as np

# arr = np.array([5, 7, 3, 9, 4, 8, 2])
# result = np.where(arr == 9)
# print(result)


# arr = np.array([5, 7, 3, 9, 4, 8, 2])
# result = np.where(arr % 2 == 0)
# print(result)


# arr = np.array([5, 7, 3, 9, 4, 8, 2])
# result = np.where(arr % 2 == 1)
# print(result)

arr = np.array([5, 6, 7, 8, 9])
# result = np.searchsorted(arr, 7)
# print(result)

result = np.searchsorted(arr, 7, side='right')
print(result)
