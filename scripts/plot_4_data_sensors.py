import pandas as pd

from src.data_labels import APARTMENT_WALKS_RICCI
from src.sensor import SensorData
import matplotlib.pyplot as plt
import os
PANDAS_WIDTH = 150
pd.set_option('display.width', PANDAS_WIDTH)

if __name__ == '__main__':
    chosen_folder = APARTMENT_WALKS_RICCI
    files = os.listdir(chosen_folder)
    for csv_file in files:
        name,ext = os.path.splitext(csv_file)
        if ext != '.csv':
            continue

        csv_file = os.path.join(chosen_folder,csv_file)
        sensordata = SensorData(csv_file)
        print name, sensordata.magnetic().shape

        fig, axs = plt.subplots(2,2, sharex=True)
        axs[0,0].plot(sensordata.orient())
        axs[0,0].set_title('Orient')
        axs[1,0].plot(sensordata.lin_acc())
        axs[1,0].set_title('Lin Acc')
        axs[1,1].plot(sensordata.gyro())
        axs[1,1].set_title('Gyro')
        axs[0,1].plot(sensordata.magnetic())
        axs[0,1].set_title('Mag')

        plt.suptitle("%s \n Measurements" %(name) )

        plt.legend()
        plt.show()
