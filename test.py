import numpy as np

state = np.ones([224, 1])
new_row = np.zeros([224, 1])
state = np.append(state, new_row, axis=1)
print(state)
state = np.transpose(state)
print(np.max(state[0]))
#