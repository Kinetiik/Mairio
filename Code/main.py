import gym
import gym_mairio
import numpy as np
from helper_functions_python import *
from gather_data import gather_data
from config import frame_count
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


def start_training_simulation():
    state = env.reset()
    run_number = 0
    frame = 0
    reset_flag = False
    action_unedited_list = []
    state_list = []
    reward_list = []
    while frame < frame_count or not reset_flag:
        print(frame)
        # around one kb of data per frame
        # Todo: fix obs space, implement unlimited time in emulator

        action_unedited = env.action_space.sample()
        action = convert_action(action_unedited)
        state, reward, reset_flag = env.step(action)
        action_unedited_list.append(action_unedited)
        state_list.append(state)
        reward_list.append(reward)
        frame += 1
        # env.render()
        if reset_flag:
            gather_data(action_unedited_list, state_list,
                        reward_list, run_number, frame)
            action_unedited_list = []
            state_list = []
            reward_list = []
            reset_reset()
            run_number += 1
            env.reset()


def start_q_table_simulation():
    q_table = load_q_table()
    encoding = load_encoding()
    state = env.reset()
    reset_flag = False
    run_number = 0
    epsilon = -1
    frame = 0
    unknown_states = 0
    while frame < frame_count or not reset_flag:
        print(np.shape(encoding))
        if random.uniform(0, 1) < epsilon:
            action_unedited = env.action_space.sample()
        else:

            action_unedited = np.argmax(
                q_table[encoding[state]])
            print("done")

            #unknown_states += 1
            #action_unedited = env.action_space.sample()
        action = convert_action(action_unedited)
        state, reward, reset_flag = env.step(action)
        frame += 1
        if reset_flag:
            reset_reset()
            run_number += 1
            env.reset()
    print(unknown_states)


if __name__ == "__main__":
    # start_training_simulation()
    # train_q_table()
    start_q_table_simulation()
