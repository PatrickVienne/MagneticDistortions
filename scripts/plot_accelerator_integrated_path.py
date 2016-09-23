import pandas as pd

from src.data_labels import APARTMENT_WALKS_BAD
from src.sensor import SensorData
import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
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
    import matplotlib.colors as colors
    import matplotlib.cm as cmx


    for csv_file in files:
        name,ext = os.path.splitext(csv_file)
        if ext != '.csv':
            continue

        csv_file = os.path.join(chosen_folder,csv_file)
        sensordata = SensorData(csv_file)
        print name, sensordata.magnetic().shape

        acc = sensordata.lin_acc()
        orient = sensordata.orient()

        # get differences in float seconds
        acc['duration[s]'] = acc.index.to_series().diff().dt.total_seconds().shift(-1).fillna(0)

        # gives very bad results, we double integrate errors
        for x in acc.columns[:-1]:
            total_change = acc_double_integrator(acc[x], acc['duration[s]'])
            acc[x+'_INT'] = total_change

        print acc.head()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        n_lines = acc.shape[0]

        jet = cm = plt.get_cmap('jet')
        cNorm = colors.Normalize(vmin=0, vmax=n_lines)
        scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)

        for i in range(n_lines):
            colorVal = scalarMap.to_rgba(i)

            vec_x = [acc.iloc[:,0].shift(1).fillna(0)[i],acc.iloc[:,0][i]]
            vec_y = [acc.iloc[:,1].shift(1).fillna(0)[i],acc.iloc[:,1][i]]
            vec_z = [acc.iloc[:, 2].shift(1).fillna(0)[i], acc.iloc[:, 2][i]]
            ax.plot(vec_x,vec_y ,zs=vec_z,color=colorVal)

            # add arrows to each line
            #a, e = zip(vec_x,vec_y,vec_z)
            #ax.scatter(a[0], a[1], a[2], color='g', marker="o")
            #ax.scatter(e[0], e[1], e[2], color='y', marker="^", s=20)
        ax.scatter(0,0,0, color='g', marker="o")
        ax.scatter(acc.iloc[-1,0], acc.iloc[-1,1], acc.iloc[-1,2], color='y', marker="^", s=20)
        plt.show()