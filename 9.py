import numpy as np
lst = list(map(float, input("Type number with space (list): ").split()))
print("Original List: ",lst)
print("List to array conversion: ")
print(np.asarray(lst))
tup= tuple(map(float, input("Type number with space (Tuple): ").split()))
print("Original Tuple: ",tup)
print("Tuple to array: ")
print(np.asarray(tup))
