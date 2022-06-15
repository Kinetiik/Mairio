import numpy as np
from helper_functions_python import *


def gather_data(action_unedited, state, reward, run_number, frame):
    reward = np.asarray(reward)
    action = np.asarray(action_unedited)
    reward = np.asarray(reward)
    with open(f"trainings_data/{run_number}.npz", "wb")as f:
        np.savez(f, state=state, action=action,
                 reward=reward)
