# coding=utf-8
import os
import matplotlib.pylab as plt

from src.data_labels import APARTMENT_WALKS_BAD
from src.fourier import filter_example
from src.sensor import SensorData

if __name__ == '__main__':

    chosen_folder = APARTMENT_WALKS_BAD
    files = os.listdir(chosen_folder)
    for csv_file in files:
        name,ext = os.path.splitext(csv_file)
        if ext != '.csv':
            continue
        csv_file = os.path.join(chosen_folder,csv_file)

        sensordata = SensorData(csv_file)

        i_col = 0
        filtered_signal1 = filter_example(sensordata.magnetic().iloc[:, i_col], fc=0.001, b=0.1)
        filtered_signal2 = filter_example(sensordata.magnetic().iloc[:, i_col], fc=0.0001, b=0.1)
        filtered_signal3 = filter_example(sensordata.magnetic().iloc[:, i_col], fc=0.001, b=0.01)
        filtered_signal4 = filter_example(sensordata.magnetic().iloc[:, i_col], fc=0.0001, b=0.01)

        filtered_signal4.plot()
        plt.title(sensordata.magnetic().columns[i_col].split('(')[0])
        plt.legend()
        plt.show()
