import numpy as np
new_row = np.empty([256, 1])


def save_encoding(encoding):
    np.save("encoding.npy", np.asarray(encoding), allow_pickle=True)


def load_encoding():
    encoding = np.load("encoding.npy", allow_pickle=True)
    return encoding


def add_row_to_q_table(table):
    table = np.append(table, new_row, axis=1)
    return table
