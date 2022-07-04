import numpy as np
from config import frame_count
import os
from encoding import *
from helper_functions_python import convert_to_string


def train_q_table():
    states, actions, rewards = read_data()
    alpha = 0.025
    gamma = 0.5
    encoding = {}
    index = 0
    q_table = np.ndarray([256, 0])

    for state, action, reward in zip(states, actions, rewards):
        for s, a, r in zip(state, action, reward):
            s = tuple(s.flatten())

            if not s in encoding:
                encoding[s] = index
                q_table = add_row_to_q_table(q_table)
                index += 1
            binary = ""
            for i in range(8):
                binary += str(a[i])
            a = int(binary, 2)

            q_value = q_table[a][encoding[s]]
            q_transposed = np.transpose(q_table)
            max_value = np.max(q_transposed[encoding[s]])
            new_q_value = (1 - alpha) * q_value + \
                alpha * (r + gamma * max_value)

            q_table[a][encoding[s]] = new_q_value
    with open("q_table.npy", "wb") as f:
        np.save(f, q_table)
    save_encoding(encoding)

    return q_table, encoding


def update_q_table(states, actions, rewards, q_table, encoding):
    alpha = 0.01
    gamma = 0.6
    index = 0
    for s, a, r in zip(states, actions, rewards):

        if not s in encoding:
            encoding[s] = index
            q_table = add_row_to_q_table(q_table)
            index += 1
        binary = ""
        for i in range(8):
            binary += str(a[i])
        a = int(binary, 2)

        q_value = q_table[a][encoding[s]]
        q_transposed = np.transpose(q_table)
        max_value = np.max(q_transposed[encoding[s]])
        new_q_value = (1 - alpha) * q_value + alpha * \
            (r + gamma * max_value)  # Todo change, record own runs

        q_table[a][encoding[s]] = new_q_value

    return q_table, encoding


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


if __name__ == "__main__":
    table, encoding = train_q_table()
