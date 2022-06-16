import numpy as np
new_row = np.empty([256, 1])


def save_enocding(encoding):
    np.save("encoding.npy")


def load_encoding():
    encoding = np.load("encoding.npy")
    return encoding


def add_row_to_q_table(table):
    table = np.append(table, new_row, axis=1)
    return table
