
import time
import numpy as np
import matplotlib.pyplot as plt
import math
inputs = {"A": False,
          "B": False,
          "Y": False,
          "X": False,
          "Left": False,
          "Right": False,
          "Up": False,
          "Down": False}

index_outputs = ["Mario_x_pos", "Mario_y_pos", "camera_x", "camera_y",
                 "sprite1_number", "sprite1_x_pos", "sprite1_y_pos",
                 "sprite2_number", "sprite2_x_pos", "sprite2_y_pos",
                 "sprite3_number", "sprite3_x_pos", "sprite3_y_pos",
                 "sprite4_number", "sprite4_x_pos", "sprite4_y_pos",
                 "sprite5_number", "sprite5_x_pos", "sprite5_y_pos",
                 "sprite6_number", "sprite6_x_pos", "sprite6_y_pos",
                 "sprite7_number", "sprite7_x_pos", "sprite7_y_pos",
                 "sprite8_number", "sprite8_x_pos", "sprite8_y_pos",
                 "sprite9_number", "sprite9_x_pos", "sprite9_y_pos",
                 "sprite10_number", "sprite10_x_pos", "sprite10_y_pos",
                 "sprite11_number", "sprite11_x_pos", "sprite11_y_pos",
                 "sprite12_number", "sprite12_x_pos", "sprite12_y_pos"]


def read_outputs_from_file(filename: str) -> dict:
    outputs = {}
    with open(filename) as file:
        file_readout = file.readlines()
        for line in file_readout:
            split_string = line.split(":")
            split_string[0] = split_string[0].strip("/n")
            outputs[split_string[0]] = int(split_string[1])
    file.close()
    return outputs


def get_data_grid():
    tile_grid = np.full((14, 16), -100)
    sprite_grid = np.full((14, 16), -100)
    with open("Code/data/map16") as file:
        file_readout = file.readlines()
        for line in file_readout:
            split_coordinates_and_data = line.split(":")
            coordinates = split_coordinates_and_data[0].split("-")
            x = int(coordinates[0])
            y = int(coordinates[1])
            tile_kind = split_coordinates_and_data[1]
            try:
                tile_grid[y, x] = tile_kind  # TODO Filter "empty" tiles
            except IndexError:
                print("indexerror")

    file.close()
    with open("Code/data/outputs") as file:
        file_readout = file.readlines()
        data = []
        for line in file_readout:
            split_string = line.split(":")
            data.append(int(split_string[1].strip("/n")))
    file.close()

    global cam_x
    global cam_y
    cam_x = data[2]
    cam_y = data[3]
    mario_x, mario_y = convert_to_relativ_coordinates(
        data[0]+16, data[1]+16)
    mario_pos = np.array((mario_x, mario_y))
    # TODO: Implement correct IDS
    #sprite_grid[mario_y, mario_x] = 123
    for i in range(12):
        sprite_number = data[4+(3*i)]
        sprite_x = data[5+(3*i)]
        sprite_y = data[6+(3*i)]
        relative_x, relative_y = convert_to_relativ_coordinates(
            sprite_x, sprite_y)
        try:
            sprite_grid[relative_y, relative_x] = sprite_number
        except IndexError:  # enemys which are offscreen
            continue

    return [tile_grid, sprite_grid, mario_pos]


def convert_to_relativ_coordinates(x, y):
    relative_x = math.floor(((x-cam_x)/16))
    relative_y = math.floor(((y-cam_y)/16))
    return relative_x, relative_y


def check_for_reset():
    with open("Code/data/reset")as file:
        text = file.readlines()
        if text == "1":  # TODO reset the text to 0 after reset
            file.close()
            return True
        else:
            file.close()
            return False


def write_inputs_to_file(filename: str, inputs: dict):
    with open(filename, "w") as file:
        lines = []
        for key in inputs:
            lines.append(f"{key}:{inputs[key]}")
        for line in lines:
            file.write(line)
            file.write('\n')
    file.close()


def wait_for_lua():
    with open("Code/data/waiting", "w") as file:
        file.write("0")  # 1 = python is executing code, 0 = lua and emulator
    file.close()
    with open("Code/data/waiting", "r") as file2:
        value = file2.read()
        while value == "0":
            file2.seek(0)
            value = file2.read()

    file2.close()


def get_reward():
    with open("Code/data/rewards", "r") as file:
        reward = file.read()
    file.close()
    return reward


def initialize():
    print("Please setup the environment manually!")

# tile_grid, sprite_grid, mario_pos = get_data_grid()
# plt.imshow(tile_grid)
# print(sprite_grid)
# plt.show()
