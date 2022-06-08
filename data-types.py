"""
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

import numpy as np

# ? Checking the Data Type of an Array

# arr = np.array([5, 6, 3, 7])
# print(arr.dtype)

# arr2 = np.array(['samsung', 'apple', 'google', 'xiaomi'])
# print(arr2.dtype)

# ? Creating Arrays With a Defined Data Type
# arr = np.array([5, 6, 3, 7], dtype='S')
# print(arr)

# arr2 = np.array([6, 4, 3, 7], dtype='i4')
# print(arr2)

# ? Converting Data Type on Existing Arrays
# ? float to integer
# arr = np.array([5.5, 7.3, 6.2])

# newArr = arr.astype('i')
# print(newArr)

# newArr = arr.astype(int)
# print(newArr)

# ? integer to boolean
arr = np.array([5, 6, 0])
newArr = arr.astype(bool)
print(newArr)
