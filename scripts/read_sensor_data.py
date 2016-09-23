import pandas as pd

from scripts.save_plot_data import APARTMENT_WALKS
from src.sensor import SensorData
import matplotlib.pyplot as plt
import os
PANDAS_WIDTH = 150
pd.set_option('display.width', PANDAS_WIDTH)

if __name__ == '__main__':
    chosen_folder = APARTMENT_WALKS
    files = os.listdir(chosen_folder)
    for csv_file in files:
        name,ext = os.path.splitext(csv_file)
        if ext != '.csv':
            continue
        print name
        csv_file = os.path.join(chosen_folder,csv_file)
        sensordata = SensorData(csv_file)
        sensordata.magnetic().plot()
        plt.show()
