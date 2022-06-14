import numpy as np
from config import frame_count
import os


def train_q_table(states, actions, rewards):
    alpha = 0.1
    gamma = 0.6
    q_table = np.zeros(
        [enviroment.observation_space.n, enviroment.action_space.n])

    for state, action, reward in zip(states, actions, rewards):
        q_value = q_table[state, action]
        max_value = np.max(q_table[next_state])
        new_q_value = (1 - alpha) * q_value + alpha * \
            (reward + gamma * max_value)

    # Update Q-table
    q_table[state, action] = new_q_value
    np.save("q_table.npy", q_table, allow_pickle=True)
    return q_table


def read_data():
    files = os.listdir("trainings_data/")
    states = []
    actions = []
    rewards = []
    for file in files:
        with open(f"trainings_data/{file}") as f:
            data = np.load(f, allow_pickle=True)
            states.append(data["state"])
            actions.append(data["action"])
            rewards.append(data["reward"])
    return np.asarray(states), np.asarray(actions), np.asarray(rewards)
