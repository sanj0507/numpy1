import numpy as np
b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
#dimension of array
print(b.ndim)
#shape of array
print(b.shape)
#data type
print(b.dtype)

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
##get a specific row
print(a[0,:])
#get a specific column
print(a[:,2])
print(a[0,1:6:2])
#0th row,from 1st index to 5th index, step size of 2
a[:,2]=5
 #to make all entries in 2nd column as 5
print(a)