import numpy as np
from helper_functions_python import *

# TODO change rewards to delta_reward


def gather_data(action_unedited, state, reward, run_number, frame):
    reward = np.asarray(reward)
    action = np.asarray(action_unedited)
    data = np.array([state, action, reward], dtype=object)
    with open(f"trainings_data/{run_number}.npy", "ab")as f:
        np.save(f, data)
