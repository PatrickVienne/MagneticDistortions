import pandas as pd

from src.data_labels import APARTMENT_WALKS_BAD
from src.sensor import SensorData
import numpy as np
import matplotlib.pyplot as plt
import os
PANDAS_WIDTH = 150
pd.set_option('display.width', PANDAS_WIDTH)

def delta_pos(a,v,dt):
    return a*dt*dt/2 + v*dt


def delta_vel(a,dt):
    return a*dt

def acc_double_integrator(acc_array,dt_array):
    vel_array = dt_array * acc_array
    vel_array = vel_array.shift(1).fillna(0)
    pos_array = dt_array * dt_array * acc_array / 2 + dt_array * vel_array
    return pos_array.cumsum()

if __name__ == '__main__':
    chosen_folder = APARTMENT_WALKS_BAD
    files = os.listdir(chosen_folder)
    for csv_file in files:
        name,ext = os.path.splitext(csv_file)
        if ext != '.csv':
            continue

        csv_file = os.path.join(chosen_folder,csv_file)
        sensordata = SensorData(csv_file)
        print name, sensordata.magnetic().shape

        acc = sensordata.lin_acc()
        gyro = sensordata.gyro()
        orient = sensordata.orient()

        # get differences in float seconds
        acc['duration[s]'] = acc.index.to_series().diff().dt.total_seconds().shift(-1).fillna(0)
        gyro['duration[s]'] = gyro.index.to_series().diff().dt.total_seconds().shift(-1).fillna(0)

        # TODO: do it with quaternions!!!, cannot just add up gyroscope values
        for i,x in enumerate(gyro.columns[:-1]):
            total_change = gyro[x] * gyro['duration[s]']
            print 'Orientation Change:', orient.iloc[-1,i] - orient.iloc[0, i], 'Gyroscope Change:', total_change.cumsum().iloc[-1]

        for x in acc.columns[:-1]:
            total_change = acc_double_integrator(pd.ewma(acc[x],span=10), acc['duration[s]'])
            print x, total_change.iloc[-1]