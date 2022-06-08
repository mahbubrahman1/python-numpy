# NumPy is used to work with arrays. The array object in NumPy is called (ndarray).
# * We can create a NumPy (ndarray) object by using the array() function.

import numpy as np

# myList = [6, 7, 3, 4]
# myArray = np.array(myList)
# print(myArray)

# different way
# myArray = np.array([3, 5, 6, 8])
# print(myArray)


# Use a tuple to create a NumPy array:
# myTuple = (6, 3, 9, 1, 8)
# myArray = np.array(myTuple)
# print(myArray)

# myArray = np.array((4, 6, 3, 8))
# print(myArray)

# ? Dimensions in Arrays

#! 0-D Arrays
# arr = np.array(56)
# print(arr)

#! 1-D Arrays
# arr = np.array([6, 8, 3, 4, 9])
# print(arr)

#! 2-D Arrays
# myArray = [[5, 3, 7], [2, 9, 6]]
# npArray = np.array(myArray)
# print(myArray)

#! 3-D Arrays
#! Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6
# myArray = [[[2, 5, 6], [5, 8, 3]], [[8, 9, 6], [3, 2, 8]]]
# npArray = np.array(myArray)
# print(myArray)


# ? Check Number of Dimensions?
# ? NumPy Arrays provides the (ndim) attribute that returns an integer that tells us how many dimensions the array have.

arr1 = np.array(56)
arr2 = np.array([6, 8, 3, 4, 9])
arr3 = np.array([[5, 3, 7], [2, 9, 6]])
arr4 = np.array([[[2, 5, 6], [5, 8, 3]], [[8, 9, 6], [3, 2, 8]]])
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)
