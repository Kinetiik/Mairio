import numpy as np


state = np.arange(2, 123)
action = np.arange(1, 8)
reward = np.array([312.123])
with open(f"test.npz", "wb")as f:
    np.savez(f, state=state, action=action,
             reward=reward)

data = np.load("test.npz", allow_pickle=True)
