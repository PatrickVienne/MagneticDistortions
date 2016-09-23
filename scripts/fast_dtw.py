import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from src.fast_dtw import dtw_plot

if __name__ == '__main__':
    n = 20
    x = np.array(zip(range(n/2),range(n/2)))
    y = np.array(zip(range(n), 2 * np.sin(range(n)) ** 2))

    distance, path = fastdtw(x, y, dist=euclidean)

    fig, axs, done_plt = dtw_plot(x, y, path, distance)
    done_plt.show()
