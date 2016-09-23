import pandas as pd

from src.data_labels import INDOORS_OFFICE
from src.sensor import SensorData
import matplotlib.pyplot as plt
import os
PANDAS_WIDTH = 150
pd.set_option('display.width', PANDAS_WIDTH)

if __name__ == '__main__':
    chosen_folder = INDOORS_OFFICE
    files = os.listdir(chosen_folder)
    for csv_file in files:
        name,ext = os.path.splitext(csv_file)
        if ext != '.csv':
            continue

        csv_file = os.path.join(chosen_folder,csv_file)
        sensordata = SensorData(csv_file)
        print name, sensordata.magnetic().shape
        sensordata.magnetic().plot()
        plt.savefig(os.path.join(chosen_folder,name+'.png'),format='png')
        plt.title(name)
        plt.close()