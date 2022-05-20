import numpy as np

data = np.full((10, 5), -1)
print(data)

for i in range(10):
    for j in range(5):
        data[i, j] = 2
print(data)
