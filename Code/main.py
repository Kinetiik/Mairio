import gym
import gym_mairio
import numpy as np
from helper_functions_python import *
from gather_data import gather_data
from config import frame_count
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
    for frame in range(frame_count):
        # if random.uniform(0, 1) < epsilon:
        #         action = enviroment.action_space.sample()
        # else:
        #         action = np.argmax(q_table[state])
        action_unedited = env.action_space.sample()
        action = convert_action(action_unedited)
        state, reward, reset_flag = env.step(action)
        gather_data(action_unedited, state, reward, run_number, frame)
        env.render()
        if reset_flag:
            reset_reset()
            run_number += 1
            env.reset()
    # TODO: Implement reinforcement learning
    
def start_q_table_simulation():
    q_table = load_q_table()
    state = env.reset()
    run_number = 0
    epsilon = 0.4
    for frame in range(frame_count):
        if random.uniform(0, 1) < epsilon:
                action_unedited = enviroment.action_space.sample()
        else:
                 action_unedited = np.argmax(q_table[state])
        action = convert_action(action_unedited)
        state, reward, reset_flag = env.step(action)
        
        if reset_flag:
            reset_reset()
            run_number += 1
            env.reset()


if __name__ == "__main__":
    start_training_simulation()
   