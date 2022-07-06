import gym
import gym_mairio
import numpy as np
from helper_functions_python import *
from gather_data import gather_data
from config import frame_count, gamma, alpha, epsilon
from train_matrix_from_data import *
from encoding import *
import random
inputs = {"A": False,
          "B": False,
          "Y": False,
          "X": False,
          "Left": False,
          "Right": False,
          "Up": False,
          "Down": False}


env = gym.make("mairio-v0")  # Create the environment


def start_q_table_simulation():
    q_table = load_q_table()
    encoding = load_encoding()

    action_unedited_list = []
    state_list = []
    reward_list = []

    state = env.reset()
    state = tuple(state.flatten())

    reset_flag = False
    run_number = 0

    frame = 0
    unknown_states = 0
    while frame < int(frame_count/4) or not reset_flag:
        if random.uniform(0, 1) < epsilon:
            action_unedited = int_to_action(env.action_space.sample())
        else:
            if state in encoding:
                index_action = np.argmax(q_table[:, encoding[state]])
                action_unedited = int_to_action(index_action)
            else:
                unknown_states += 1
                action_unedited = int_to_action(env.action_space.sample())

        action = convert_action(action_unedited)
        state, reward, reset_flag = env.step(action)
        print(frame, reward)
        state = tuple(state.flatten())
        frame += 1
        action_unedited_list.append(action_unedited)
        state_list.append(state)
        reward_list.append(reward)
        if reset_flag:

            try:
                for i in range(1, 8):
                    reward_list[len(reward_list)-i] -= 2000
            except IndexError:
                pass

            q_table, encoding = update_q_table(
                state_list, action_unedited_list, reward_list, q_table, encoding)
            # gather_data(action_unedited_list, state_list,
            # reward_list, run_number, frame)
            action_unedited_list = []
            state_list = []
            reward_list = []
            reset_reset()
            run_number += 1
            env.reset()
    print("unknown:", unknown_states)

    save_encoding(encoding)
    with open("q_table.npy", "wb") as f:
        np.save(f, q_table)


if __name__ == "__main__":
    start_q_table_simulation()
