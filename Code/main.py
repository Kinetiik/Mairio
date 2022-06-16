import gym
import gym_mairio
import numpy as np
from helper_functions_python import *
from gather_data import gather_data
from config import frame_count
from train_matrix_from_data import *
from encoding import *
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
    reset_flag = False
    action_unedited_list = []
    state_list = []
    reward_list = []
    while frame < frame_count or not reset_flag:

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
    # TODO: Implement reinforcement learning


def start_q_table_simulation():
    q_table = load_q_table()
    encoding = load_encoding()
    state = env.reset()
    reset_flag = False
    run_number = 0
    epsilon = 0.4
    while frame < frame_count or not reset_flag:
        if random.uniform(0, 1) < epsilon:
            action_unedited = enviroment.action_space.sample()
        else:
            try:
                action_unedited = np.argmax(
                q_table[np.where(encoding == state)])
            except:
                action_unedited = enviroment.action_space.sample()
        action = convert_action(action_unedited)
        state, reward, reset_flag = env.step(action)
        frame += 1
        if reset_flag:
            reset_reset()
            run_number += 1
            env.reset()


if __name__ == "__main__":
    # start_training_simulation()
    states, actions, rewards = read_data()
    q_table = train_q_table(states, actions, rewards, env)
    print(np.shape(q_table))
