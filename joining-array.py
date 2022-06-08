import numpy as np

# arr1 = np.array([5, 7, 3])
# arr2 = np.array([8, 4, 9])
# print(np.concatenate((arr1, arr2)))


# arr1 = np.array([[2, 5], [8, 6]])
# arr2 = np.array([[3, 4], [2, 9]])
# newArray = np.concatenate((arr1, arr2), axis=1)
# print(newArray)

arr1 = np.array([6, 7, 8])
arr2 = np.array([5, 2, 1])
arr = np.hstack((arr1, arr2))
print(arr)
