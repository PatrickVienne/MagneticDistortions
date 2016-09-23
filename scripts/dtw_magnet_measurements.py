import pandas as pd
from scipy.spatial.distance import euclidean
import numpy as np
from src.data_labels import APARTMENT_WALKS_BAD, APARTMENT_WALKS_IBO, APARTMENT_WALKS_RICCI
from src.fast_dtw import dtw_plot
from fastdtw import fastdtw
from src.sensor import SensorData
import matplotlib.pyplot as plt
import os
PANDAS_WIDTH = 150
pd.set_option('display.width', PANDAS_WIDTH)


if __name__ == '__main__':
    data_sets = [APARTMENT_WALKS_BAD,APARTMENT_WALKS_RICCI,APARTMENT_WALKS_IBO]
    trainings = []
    tests = []

    # populate trainings and tests with our files
    for chosen_folder in data_sets:
        files = os.listdir(chosen_folder)
        get_test = True
        for csv_file in files:
            name, ext = os.path.splitext(csv_file)
            if ext != '.csv':
                continue
            csv_file = os.path.join(chosen_folder, csv_file)
            sensordata = SensorData(csv_file)
            if get_test:
                print 'Added to Test', name
                tests.append(sensordata.magnetic())
                get_test = False
            else:
                print 'Added to Trainings', name
                trainings.append(sensordata.magnetic())

    print "Test", len(tests)
    print "Trainings", len(trainings)
    result_matrix = np.zeros((len(tests),len(trainings)))

    for j,t in enumerate(tests):
        for k,tr in enumerate(trainings):
            sum = 0
            for i in range(3):
                x = np.array(zip(t.iloc[:, i].index.to_series().diff().dt.total_seconds().fillna(0).cumsum().values, t.iloc[:, i]))
                y = np.array(zip(tr.iloc[:, i].index.to_series().diff().dt.total_seconds().fillna(0).cumsum().values, tr.iloc[:, i]))
                distance, path = fastdtw(x, y, dist=euclidean)
                fig, axs, done_plt = dtw_plot(x, y, path, distance)
                plt.close()
                #done_plt.show()
                sum += distance
            print j,k,distance
            result_matrix[j,k] = sum
    print result_matrix
