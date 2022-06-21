import numpy as np
from config import frame_count
import os
from encoding import *


def train_q_table(states, actions, rewards, env):
    alpha = 0.1
    gamma = 0.6
    encoding = np.array()
    q_table = np.empty([256, 0])

    for state, action, reward in zip(states, actions, rewards):
        for s, a, r in zip(state, action, reward):
            if s not in encoding: #TODO Change to work with arrays correctly
                encoding = np.append(encoding, s)
            binary = ""
            for i in range(8):
                binary += str(a[i])
            a = int(binary, 2)

            q_value = q_table[a][np.where(encoding == s)]
            max_value = np.max(np.transpose(q_table)[np.where(encoding == s)])
            new_q_value = (1 - alpha) * q_value + \
                alpha * (r + gamma * max_value)

            q_table[a][np.where(encoding == s)] = new_q_value
    np.save("q_table.npy", q_table)
    save_enocding(encoding)
    return q_table


def read_data():
    files = os.listdir("trainings_data/")
    states = []
    actions = []
    rewards = []
    for file in files:
        data = np.load(f"trainings_data/{file}")

        states.append(data["state"])
        actions.append(data["action"])
        rewards.append(data["reward"])  # TODO Fix reward

    return np.asarray(states, dtype=object), np.asarray(actions, dtype=object), np.asarray(rewards, dtype=object)
