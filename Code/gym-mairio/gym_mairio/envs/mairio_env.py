import gym
from gym import error, spaces, utils
from gym.utils import seeding
from Code.helper_functions_python import check_for_reset, wait_for_lua, initialize, get_reward, get_data_grid, write_inputs_to_file


class MairioEnv(gym.Env):

    def __init__(self):
        metadata = {'render.modes': ['human']}
        self.inputs = {"A": False,
                       "B": False,
                       "Y": False,
                       "X": False,
                       "Left": False,
                       "Right": False,
                       "Up": False,
                       "Down": False}
        self.state_map16 = np.full((14, 16), -100)
        self.state_sprites = np.full((14, 16), -100)
        self.layer_pos = [0, 0]
        self.reward = 0
        self.reset_flag = 0
        initialize()

    def step(self, action: dict):
        write_inputs_to_file("Code/data/inputs", action)
        wait_for_lua()
        self.state_map16, self.state_sprites, self.player_pos = get_data_grid()
        self.reward = get_reward()
        self.reset_flag = check_for_reset()
        return self.state_map16, self.state_sprites, self.player_pos, self.reward, self.reset_flag

    def reset(self):
        self.inputs = {"A": False,
                       "B": False,
                       "Y": False,
                       "X": False,
                       "Left": False,
                       "Right": False,
                       "Up": False,
                       "Down": False}
        self.state_map16 = np.full((14, 16), -100)
        self.state_sprites = np.full((14, 16), -100)
        self.layer_pos = [0, 0]
        self.reward = 0
        self.reset_flag = 0

    def render(self, mode='human', close=False):
        tile_grid, sprite_grid, mario_pos = get_data_grid()
        plt.imshow(tile_grid)
        print(sprite_grid)
        plt.show()
