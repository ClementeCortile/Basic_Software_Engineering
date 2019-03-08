print("Running python script")

import sys
import numpy as np
import time

X = sys.argv[1]
Y = sys.argv[2]

print("Creating a matrix")
matrix = np.random.randint(9, size=(3,3))

time.sleep(2) # Wait for 5 seconds

m = matrix.item((0,1))


print("The element at position", X, "and", Y, "is:", m )
