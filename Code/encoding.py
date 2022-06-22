import numpy as np
new_row = np.empty([256, 1])


def save_encoding(encoding):

    np.save("encoding.npy", np.asarray(
        list(encoding.keys())), allow_pickle=True)


def load_encoding():
    encoding_list = np.load("encoding.npy", allow_pickle=True)
    encoding = {}
    index = 0
    for state in encoding_list:
        state = tuple(state.flatten())
        encoding[state] = index
        index += 1
    return encoding


def add_row_to_q_table(table):
    table = np.append(table, new_row, axis=1)
    return table
