import numpy as np

# Method of creating arrays :--

"""
Creating array using value of zero
"""

zero = np.zeros((5,10)) #Enter the shape
print(f"The value of zero array is:\n {zero}")
print()

"""
Creating array using value of one only 
"""

one = np.ones((5,10))
print(f"The value of one array is:\n {one}")
print()

"""
Creating array for an specific value only like I want 10 only in my array
"""

full = np.full((5,10),10)
print(f"The value of full array is:\n {full}")
print()

"""
Creating array with random value only
"""

ran = np.empty((3,3))
print(f"The value of random array is:\n {ran}")
print()

"""
Creating array of sequence
"""

con = np.arange(0,100,3) # First value : start , Second value : Stop, Third value : step or jump
print(f"The value of sequence array is:\n {con}")
print()