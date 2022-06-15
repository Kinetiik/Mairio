import numpy as np
from config import frame_count
import os


def train_q_table(states, actions, rewards, env):
    alpha = 0.1
    gamma = 0.6
    q_table = np.zeros(shape=[14*16*25, 2**8])

    for state, action, reward in zip(states, actions, rewards):
        for s, a, r in zip(state, action, reward):
            print(s, a, r)
            q_value = q_table[s, a]
            max_value = np.max(q_table[next_state])
            new_q_value = (1 - alpha) * q_value + alpha * \
                (r + gamma * max_value)

            q_table[state, action] = new_q_value
    np.save("q_table.npy", q_table)
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
