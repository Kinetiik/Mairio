import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from train_matrix_from_data import read_data

fps = 100
seconds = 120
states, _, _ = read_data()

snapshots = []

for state in states:
    for s in state:
        s = np.reshape(s, (14, 16))
        snapshots.append(s)

fig = plt.figure(figsize=(8, 8))

a = snapshots[0]

im = plt.imshow(a, interpolation="none", aspect="auto", vmin=0, vmax=25)


def animate_func(i):
    if i % fps == 0:
        pass
    im.set_array(snapshots[i])
    return [im]


anim = animation.FuncAnimation(
    fig, animate_func, frames=seconds*fps, interval=1000/fps,)

anim.save("computer_vision.gif", fps=fps)
plt.show(anim)
