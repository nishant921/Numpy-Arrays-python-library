# What is numpy?
# NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

# At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays of homogeneous data types

# Numpy Arrays Vs Python Sequences
# NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original.

# The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory.

# NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences.

# A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays.

import numpy as np 

# Creating Numpy Arrays
# 1.
a=np.array([1,2,21])
print(a)
print(type(a))

# 2.
# 2D OR 3D array
a = np.array([[1,2,3],[4,5,6]])
print(a)

# 3D
a = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(a)
a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)

# 3.
#dtype=
f = np.array([1,2,3],dtype = float) 
print(f)
f = np.array([-1,0,3],dtype = bool) 
print(f)
f = np.array([1,2,3],dtype = complex) 
print(f)

# 4.
# arange
n = np.arange(1,13)
print(n)

# 5.
# reshape(row,col)
n = np.arange(1,13)
print(n.reshape(4,3))

# 6.
# ones and zeros
print(np.ones((4,5)))
print(np.zeros((4,5)))

# 7.
# random
n = np.random.random((2,1))
print(n)

# 8.
# linspace(range,np.of items): linear spaces -> in given range generate items with equal spaces
n = np.linspace(-10,10,10)
print(n)
# check equal spaces: distance
for i in range(len(n)-1):
        print(n[i]-n[i+1])

# 9.
# identity : like identity matrix
m = np.identity(4)
print("identity matrix: \n",m)

# 10. eye
e = np.eye(3)
print(e)
e = np.eye(3,k=1)
print(e)