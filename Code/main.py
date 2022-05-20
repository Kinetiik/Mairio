from helper_functions_python import get_data_grid, wait_for_lua, check_for_reset, write_inputs_to_file, get_reward
#from reinforcement_learning import empty


def start_game():
    running = True
    while running:
        if not check_for_reset():
            tile_data, sprite_data, player_position = get_data_grid()
            # get output from environment and return inputs
            write_inputs_to_file("data/inputs", inputs)
            wait_for_lua()
            reward = get_reward()
        else:
            # reset environment and client
            pass


if __name__ == "__main__":
    start_game()
