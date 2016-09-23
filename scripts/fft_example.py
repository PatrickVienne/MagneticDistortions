import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    t = np.linspace(0, 2 * np.pi, 1000, endpoint=True)
    f = 3.0  # Frequency in Hz
    A = 100.0  # Amplitude in Unit
    s = A * np.sin(2 * np.pi * f * t)  # Signal

    dt = t[1] - t[0]
    fa = 1.0 / dt  # scan frequency
    print('dt=%.5fs (Sample Time)' % dt)
    print('fa=%.2fHz (Frequency)' % fa)


    plt.plot(t, s)
    plt.xlabel('Time ($s$)')
    plt.ylabel('Amplitude ($Unit$)')
    plt.show()

    Y = np.fft.fft(s)
    N = len(Y) / 2 + 1
    FFT_s = np.abs(Y[:N])
    #plt.plot(FFT_s)

    X = np.linspace(0, fa / 2, N, endpoint=True)
    plt.plot(X, 2.0 * np.abs(Y[:N]) / N)
    plt.xlabel('Frequency ($Hz$)')
    plt.ylabel('Amplitude ($Unit$)')
    plt.show()

    hann = np.hanning(len(s))
    hamm = np.hamming(len(s))
    black = np.blackman(len(s))

    plt.figure(figsize=(8, 3))
    plt.subplot(131)
    plt.plot(hann)
    plt.title('Hanning')
    plt.subplot(132)
    plt.plot(hamm)
    plt.title('Hamming')
    plt.subplot(133)
    plt.plot(black)
    plt.title('Blackman')
    plt.tight_layout()

    plt.plot(t, hann * s)
    plt.xlabel('Time ($s$)')
    plt.ylabel('Amplitude ($Unit$)')
    plt.title('Signal with Hanning Window function applied')

    Yhann = np.fft.fft(hann * s)

    plt.figure(figsize=(7, 3))
    plt.subplot(121)
    plt.plot(t, s)
    plt.title('Time Domain Signal')
    plt.ylim(np.min(s) * 3, np.max(s) * 3)
    plt.xlabel('Time ($s$)')
    plt.ylabel('Amplitude ($Unit$)')

    plt.subplot(122)
    plt.plot(X, 2.0 * np.abs(Yhann[:N]) / N)
    plt.title('Frequency Domain Signal')
    plt.xlabel('Frequency ($Hz$)')
    plt.ylabel('Amplitude ($Unit$)')

    plt.annotate("FFT",
                 xy=(0.0, 0.1), xycoords='axes fraction',
                 xytext=(-0.8, 0.2), textcoords='axes fraction',
                 size=30, va="center", ha="center",
                 arrowprops=dict(arrowstyle="simple",
                                 connectionstyle="arc3,rad=0.2"))
    plt.tight_layout()

    plt.savefig('FFT.png', bbox_inches='tight', dpi=150, transparent=True)