import numpy as np

A = np.eye(2)
print "A", A
# [
#     [ 1. 0.]
#     [ 0. 1.]
# ]

B = 2 * A
print "B", B
# [
#     [ 2. 0.]
#     [ 0. 2.]
# ]

print "Compound matrix\n", np.bmat("A B; A B")
# [
#     [ 1. 0. 2. 0.]
#     [ 0. 1. 0. 2.]
#     [ 1. 0. 2. 0.]
#     [ 0. 1. 0. 2.]
# ]