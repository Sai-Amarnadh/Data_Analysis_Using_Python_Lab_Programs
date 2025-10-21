#allclose
import numpy as np
a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
print("a ≈ b (allclose):", np.allclose(a, b))