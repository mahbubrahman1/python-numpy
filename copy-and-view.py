# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

import numpy as np

# arr = np.array([5, 6, 3, 7])
# temp = arr.copy()
# arr[0] = 9

# print(arr)
# print(temp)
# The copy SHOULD NOT be affected by the changes made to the original array.


arr = np.array([5, 6, 3, 7])
temp = arr.view()
arr[1] = 9

print(arr)
print(temp)
# The view SHOULD be affected by the changes made to the original array.
