from helper_functions_python import get_data_grid, wait_for_lua, check_for_reset, write_inputs_to_file, get_reward
#from reinforcement_learning import empty


def start_game():
    running = True
    while running:
        if not check_for_reset():
            data = get_data_grid()
            # get output from environment and return inputs
            write_inputs_to_file("data/inputs", inputs)
            reward = get_reward()
            wait_for_lua()
        else:
            # reset environment and client
            pass


if __name__ == "__main__":
    start_game()
