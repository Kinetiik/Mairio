
import time
import numpy as np
import matplotlib.pyplot as plt
import math

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

IDS = {"0x15e": 1,
       "0x1ee": 1,
       "0x159": 1,
       "0x130": 1,
       "0x135": 1,
       "0x136": 1,
       "0x13d": 1,
       "0x13e": 1,
       "0x153": 1,
       "0x154": 1,
       "0x155": 1,
       "0x1aa": 2,
       "0x1e2": 2,
       "0xa1": 2,
       "0x133": 3,
       "0x134": 3,
       "0x1c4": 4,
       "0x1c7": 4,
       "0x1c6": 5,
       "0x1c5": 5,
       "0x00": 6,
       "0xbd": 6,
       "0x02": 6,
       "0x01": 6,
       "0x03": 6,
       "0x9f": 7,
       "0xab": 8,
       "0x83": 9,
       "0x2b": 10,
       "0x4f": 12,
       "0x11e": 13,
       "0x35": 14,
       "0x30": 14,
       "0x32": 14,
       "0x33": 14,
       "0x2f": 14,
       "0xb9": 15,
       "0x106": 16,
       "0x05": 17,
       "0x11f": 18,
       "0x100": 19,
       "0x101": 19,
       "0x104": 19,
       "0x145": 19,
       "0x1e2": 19,
       "0x95": 20,
       "0x3a": 21,
       "0x3d": 21,
       "0x39": 21,
       "0x3c": 21,
       "0x7b": 21,
       "0x1e4": 22,
       "0x1af": 22,
       "0x132": 22,
       "0x13b": 23,
       "0x13f": 23
       }


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


def filter_outputs(Inputs: dict):
    if Inputs["Right"] and Inputs["Left"]:
        Inputs["Right"] = True
        Inputs["Left"] = False
    if Inputs["Up"] and Inputs["Down"]:
        Inputs["Up"] = False
        Inputs["Down"] = False
    return Inputs


def get_data_grid():
    grid = np.full((14, 16), -1)

    with open("Code/data/map16") as file:
        file_readout = file.readlines()
        for line in file_readout:
            split_coordinates_and_data = line.split(":")
            coordinates = split_coordinates_and_data[0].split("-")
            x = int(coordinates[0])
            y = int(coordinates[1])
            tile_kind = split_coordinates_and_data[1]
            try:
                if hex(int(tile_kind)) in IDS:
                    grid[y, x] = IDS[hex(int(tile_kind))]
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

    for i in range(12):
        sprite_number = data[4+(3*i)]
        sprite_x = data[5+(3*i)]
        sprite_y = data[6+(3*i)]
        relative_x, relative_y = convert_to_relativ_coordinates(
            sprite_x, sprite_y)
        try:
            if hex(sprite_number) in IDS:
                grid[relative_y, relative_x] = IDS[hex(sprite_number)]
            elif hex(sprite_number) == "0x74":
                grid[relative_y, relative_x] = 11

        except IndexError:  # enemys which are offscreen
            continue

    mario_x, mario_y = convert_to_relativ_coordinates(
        data[0], data[1]+16)
    grid[mario_y, mario_x] = 24
    np.place(grid, grid == -1, 0)
    return grid


def convert_to_decimal(value):
    return int(value, 16)


def convert_to_relativ_coordinates(x, y):
    relative_x = math.ceil(((x-cam_x)/16))
    relative_y = math.ceil(((y-cam_y)/16))
    if relative_x > 15:
        relative_x = 15
    if relative_y > 13:
        relative_y = 13
    return relative_x, relative_y


def check_for_reset():
    with open("Code/data/reset")as file:
        text = file.readlines()
        if text == ['1']:  # TODO reset the text to 0 after reset
            return True
        else:
            return False


def reset_reset():
    with open("Code/data/reset", "w")as file:
        file.write("0")


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
        split_string = reward.split(":")
        reward = float(split_string[1].strip("/n"))
    file.close()
    return reward


def convert_action(action):
    edited_action = {"A": bool(action[0]),
                     "B": bool(action[1]),
                     "Y": bool(action[2]),
                     "X": bool(action[3]),
                     "Left": bool(action[4]),
                     "Right": bool(action[5]),
                     "Up": bool(action[6]),
                     "Down": bool(action[7])}
    return filter_outputs(edited_action)


def initialize():
    print("Please setup the environment manually!")


def load_q_table():
    with open("q_table.npy") as f:
        q_table = np.load(f, allow_pickle=True)
    return q_table
