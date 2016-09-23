# coding=utf-8
import pandas as pd
import numpy as np

PANDAS_WIDTH = 150
pd.set_option('display.width', PANDAS_WIDTH)




# Compute sinc filter.
def sinc_filter(fc, n, N):
    h = np.sinc(2 * fc * (n - (N - 1) / 2.))
    return h


def get_sinc_filter(fc, N, n):
    h = sinc_filter(fc, n, N)
    w = np.blackman(N)
    # Multiply sinc filter with window.
    h = h * w

    # Normalize to get unity gain.
    h = h / np.sum(h)
    return h


def filter_example(s, fc=0.001, b=0.08):
    """

    :param s:
    :param fc:  Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
    :param b: Transition band, as a fraction of the sampling rate (in (0, 0.5)).
    :return:
    """

    N = int(np.ceil((4 / b)))
    if not N % 2: N += 1  # Make sure that N is odd.
    n = np.arange(N)

    # get the sinc filter
    h = get_sinc_filter(fc, N, n)
    index = s.index
    # convolce with the signal
    s = np.convolve(s, h)

    # adjust the shifts to get the right timestamps
    s = s[np.floor(h.shape[-1] / 2.0): -np.ceil(h.shape[-1] / 2.0)+1]

    # add timestamps to the filtered series
    s = pd.Series(s, index=index)

    return s


def blackman_window(n, N):
    # Compute Blackman window.
    w = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + \
        0.08 * np.cos(4 * np.pi * n / (N - 1))
    return w
