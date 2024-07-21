xi = [1,2,3]
wi = [0.4,0.6,-0.3]
bias = 2
output = 0

for i in range(len(xi)):
    output += i * wi[i]
output += bias
print(output)
