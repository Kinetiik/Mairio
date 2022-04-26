import keras
import numpy as np

# Configuration parameters for the whole setup
seed = os.time()
gamma = 0.99  # Discount factor for past rewards
max_steps_per_episode = 10000
env = gym.make("CartPole-v0")  # Create the environment
env.seed(seed)
# Smallest number such that 1.0 + eps != 1.0
eps = np.finfo(np.float32).eps.item()


