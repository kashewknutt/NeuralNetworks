'''
This is a basic structure of a neuron.

The neuron has 3 inputs and 3 weights. The bias is 2.
It calculates output on the sum of product of inputs and weights.


'''



import numpy as np


xi = [1,2,3]
wi = [0.4,0.6,-0.3]
bias = 2
output = 0

for i in range(len(xi)):
    output += xi[i] * wi[i]
output += bias
print(output)

output = 0


output = bias + np.dot(xi,wi)
print(output)