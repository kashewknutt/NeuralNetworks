'''
This is a simple example of a layer of neurons.
It calculates 3 outputs for 3 neurons from 4 inputs.
The weights are stored in a list of lists. 
Numpy dot function is a major part of neural networks.

'''



import numpy as np


inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1],
 [0.5, -0.91, 0.26, -0.5],
 [-0.26, -0.27, 0.17, 0.87]]

weights1 = weights[0] 
weights2 = weights[1] 
weights3 = weights[2] 

biases = [2, 3, 0.5]

bias1 = 2
bias2 = 3
bias3 = 0.5

outputs = [
inputs[0]*weights1[0] +
inputs[1]*weights1[1] +
inputs[2]*weights1[2] +
inputs[3]*weights1[3] + bias1,

inputs[0]*weights2[0] +
inputs[1]*weights2[1] +
inputs[2]*weights2[2] +
inputs[3]*weights2[3] + bias2,

inputs[0]*weights3[0] +
inputs[1]*weights3[1] +
inputs[2]*weights3[2] +
inputs[3]*weights3[3] + bias3]

print(outputs)

outputs = biases + np.dot(weights, inputs)
print(outputs)

listedInputs = [[1,2,3,1.3], [3,5,2,6], [5,3,5.6,2]]

outputs = np.dot(listedInputs, np.array(weights).T) + biases
print(outputs)