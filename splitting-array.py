# ? Splitting is reverse operation of Joining.

import numpy as np

# arr = np.array([7, 5, 4, 9, 3, 2])
# newArr = np.array_split(arr, 2)
# print(newArr)

arr = np.array([7, 5, 4, 9, 3, 2])
newArr = np.array_split(arr, 3)
# print(newArr)

print(newArr[0])
print(newArr[1])
print(newArr[2])
