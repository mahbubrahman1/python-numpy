import numpy as np

# Creating numpy arrays from python lists



# my_list = [5, 7, 3, 4]
# my_numpy_list = np.array(my_list)
# print(my_numpy_list)


# second_list = [[3, 7, 2], [8, 2, 3], [9, 6, 5]]
# my_second_array = np.array(second_list)
# print(my_second_array)


#---------------------------------


# Creating NumPy array using arange() built-in function.



# my_list = np.arange(10)
# print(my_list)


# jur songkha gula print korbe. list a jemon loop use kore korte hoy kintu numpy a built in arange funtion diyei ta kora jay
# even_list = np.arange(0, 11, 2)
# print(even_list)


# jodi amar 7 ta 0 dorkar hoy
# my_zeros = np.zeros(7)
# print(my_zeros)


# jodi amar 5 ta 1 dorkar hoy
# my_ones = np.ones(5)
# print(my_ones)

# generate a two-dimensional array of zeros having 3 rows and 5 columns
# my_list = np.zeros((3, 5))
# print(my_list)

# my_second_list = np.ones((5, 5))
# print(my_second_list)


#-------------------------------------

# Creating an identity matrix in NumPy

# my_matrx = np.eye(6)
# print(my_matrx)


# my_second_matrx = np.eye(4)
# print(my_second_matrx)



#-------------------------------------

# Generating an array of random numbers in NumPy

# my_rand_num = np.random.rand(5)
# print(my_rand_num)


# my_rand_num = np.random.randn(7)
# print(my_rand_num)

# return single number
# my_rand = np.random.randint(20)
# print(my_rand)


# my_rand_num = np.random.randn(3, 3)
# print(my_rand_num)



#-------------------------------------


# Locating the maximum and minimum values of a NumPy Array

# my_array = np.arange(20)
# print(my_array.max())


# my_array = np.random.randint(0, 20, 5)
# print(my_array.max())


# my_array = np.random.randint(0, 20, 5)
# print(my_array.min())
# print(my_array.argmax())



#-------------------------------------
# Indexing/Selecting elements or groups of elements from a NumPy array

# my_array = np.arange(0, 11)
# print(my_array[10])

# print(my_array[2:6])

# print(my_array[:6])


# my_array = np.array([[10, 30, 60], [70, 30, 20], [80, 40, 30]])
# print(my_array[1][2])

# print(my_array[0][1])
# print(my_array[0, 1])


new_array = np.arange(5, 15)
if new_array > 10:
	print("True")
else:
	print("False")