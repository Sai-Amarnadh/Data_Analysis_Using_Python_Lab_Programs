#Repr,Bincount and Unique
import numpy as np
a = np.array([1, 2, 1, 3, 2, 1, 4])
print("Repr:", repr(a))
print("Bincount:", np.bincount(a))
print("Unique values:", np.unique(a))