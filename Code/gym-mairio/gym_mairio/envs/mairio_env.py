import gym
from gym import error, spaces, utils
from gym.utils import seeding
from helper_functions_python import *
from gym.spaces import Dict


class MairioEnv(gym.Env):

    def __init__(self):
        metadata = {'render.modes': ['human']}

        self.action_space = spaces.Tuple((spaces.Discrete(2), spaces.Discrete(2), spaces.Discrete(
            2), spaces.Discrete(2), spaces.Discrete(2), spaces.Discrete(2), spaces.Discrete(2), spaces.Discrete(2)))
        self.observation_space = spaces.Box(
            low=-1, high=25, shape=([14, 16]), dtype=np.float32)
        self.inputs = {"A": False,
                       "B": False,
                       "Y": False,
                       "X": False,
                       "Left": False,
                       "Right": False,
                       "Up": False,
                       "Down": False}
        self.state = None
        self.reward = 0
        self.reset_flag = 0
        initialize()

    def step(self, action: dict):
        write_inputs_to_file("Code/data/inputs", action)
        wait_for_lua()
        self.state = get_data_grid()
        self.reward = get_reward()
        self.reset_flag = check_for_reset()
        return self.state, self.reward, self.reset_flag

    def reset(self):
        self.inputs = {"A": False,
                       "B": False,
                       "Y": False,
                       "X": False,
                       "Left": False,
                       "Right": False,
                       "Up": False,
                       "Down": False}
        self.state = np.full((14, 16), -1, dtype=np.float32)
        self.reward = 0
        self.reset_flag = 0
        return self.state

    def render(self, mode='human', close=False):
        grid = get_data_grid()
        # print(grid.shape)

        plt.imshow(grid)
        plt.show()
