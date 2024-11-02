#a = [1, 2, 3, 4, 5]
#b = [10, 11, 12, 13, 14]

#result = []
#for first, second in zip(a,b):
 #   result.append(first+second)
#print(result)

# The upper method is fine but it is too difficult to write for loop again and
#again for the same things, thats why numpy comes in

import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(type(a))
# ndarray means n-dimensional array

print(a.dtype)
# dtype means data type and is used to define that array conatins float or integers

f = np.array([1.2,2.8,5.02,9.8])
print(f.dtype)

a[1] = 10
print(a[1])

#print(a.ndim)
#ndim means number of dimensions 

#print(f.shape)
# shape is always a tupple showing no of elements in the array

#print(a.size)
# size is always an integer and similar to shape


