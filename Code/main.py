import gym_mairio
import gym
import numpy as np
from helper_functions_python import *
inputs = {"A": False,
          "B": False,
          "Y": False,
          "X": False,
          "Left": False,
          "Right": False,
          "Up": False,
          "Down": False}


env = gym.make("mairio-v0")  # Create the environment


def start_simulation():
    state = env.reset()

    for _ in range(100):
        action = env.action_space.sample()
        

        pass


if __name__ == "__main__":
    start_simulation()
