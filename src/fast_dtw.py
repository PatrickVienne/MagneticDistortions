# get dtw connections
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc


def dtw_plot(x, y, path, distance):
    fig, axs = plt.subplots(1, 3)


    axs[0].plot(x[:, 0], x[:, 1], color="green", label='x')
    axs[0].plot(y[:, 0], y[:, 1], color="red", label='y')


    axs[1].scatter(x=np.array(path)[:, 0], y=np.array(path)[:, 1], label='dtw:path')

    # create lines using the paths data and the dataframes
    lines = [[x[p1], y[p2]] for p1, p2 in zip(np.array(path)[:, 0], np.array(path)[:, 1])]
    # add to line collection
    lc = mc.LineCollection(lines, linewidths=2, label='dtw:shortest')
    # plot the line collection
    axs[2].add_collection(lc)
    axs[2].autoscale()
    axs[2].margins(0.1)
    axs[2].plot(x[:, 0], x[:, 1], color="green", label='x')
    axs[2].plot(y[:, 0], y[:, 1], color="red", label='y')

    # show all legends
    for ax in axs:
        ax.legend()

    plt.suptitle("DTW - TEST \n Distance:%f"%distance)

    return fig, axs, plt


