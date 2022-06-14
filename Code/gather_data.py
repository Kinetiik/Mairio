import numpy as np
from helper_functions_python import *


def gather_data(action_unedited, state, reward, run_number, frame):
    reward = np.asarray(reward)
    action = np.asarray(action_unedited)
    with open(f"trainings_data/{run_number}.npz", "ab")as f:
        np.savez(f, state=state, action=action,
                 reward=reward, allow_pickle=True)
