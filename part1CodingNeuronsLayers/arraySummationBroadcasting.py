import numpy as np
inputs = [[0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100, 100], [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100, 100], [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100, 100]]
output = np.maximum(0, inputs)
print(output)
print("Twice:", np.sum(np.array(inputs), axis=None))

print("Twice:", np.sum(np.array(inputs), axis=0))

print("Twice:", np.sum(np.array(inputs), keepdims=True))