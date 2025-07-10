import numpy as np
from Init_simplex import init_simplex

B = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 1]])
K = np.identity(3)
x = np.array([5.0, -1.0, 5.0, -10.0, 8.0])
In = np.array([4, 5, 6, 7])
Ib = np.array([0, 1, 2, 3])

## Example

A = np.array([[1.0, 0.0, 1.0, 0.0, 0.0],
              [0.0, 1.0, 0.0, 1.0, 0.0],
              [3.0, 2.0, 0.0, 0.0, 1.0],
              ])

b = np.array([4.0, 6.0, 18.0])

c = np.array([3.0, 5.0, 0.0, 0.0, 0.0])

x = np.array([0.0, 0.0, 4.0, 6.0, 18.0])



init_simplex(A, b, c, x)
