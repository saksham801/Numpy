import numpy as np
import time

'''
Creating array using numpy
'''

array_1d = np.array([1,2,3,4,5]) # 1D Array
print(f"1d array:\n {array_1d}")
print()


'''
Creating 2d array
'''

array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]]) #2D Array
print(f"2d array:\n {array_2d}")
print()

'''
Creating 3D array
'''

array_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]]) #3D Array
print(f"3d array:\n {array_3d}")
print()


"""
List vs Array
"""

"Creating List and multiplying it with any number"

list_1 = [1,2,3,4,5]
print(f"Multiplication of list:\n {list_1 * 2}")
print()

"Creating Array and multiplying it with any number"

array_4 = np.array([1,2,3,4,5,6])
print(f"Multiplication of array: {array_4 * 2}") # Element wise multiplication it like a simple multiplication one by one
print()

"""
Calulating the time
"""


start = time.time()

py_mut = [i *2 for i in range(1000000000)] # It not run or it fail to run memory error
print(f' The Time in list {time.time()-start} ')

arrad = np.arange(1000000000) * 2
print(f' The Time in Array {time.time()-start} ') # It take 67 sec