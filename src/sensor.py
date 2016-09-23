import datetime
import pandas as pd

class SensorData():

    def __init__(self, path):
        self.TIME_COL = 'YYYY-MO-DD HH-MI-SS_SSS'
        self.date_parser_format = '%Y-%m-%d %H:%M:%S:%f'
        self.data = pd.read_csv(path, parse_dates=[self.TIME_COL], date_parser=self.parse_date)
        self.columns = self.data.columns
        self.data.set_index(self.TIME_COL, inplace=True)

    def parse_date(self, date_str):
        return datetime.datetime.strptime(date_str, self.date_parser_format)

    def magnetic(self):
        return self.data[[x for x in self.columns if x.startswith('MAGNETIC FIELD')]]

    def gyro(self):
        return self.data[[x for x in self.columns if x.startswith('GYROSCOPE')]]

    def lin_acc(self):
        return self.data[[x for x in self.columns if x.startswith('LINEAR ACCELERATION')]]

    def acc(self):
        return self.data[[x for x in self.columns if x.startswith('ACCELEROMETER')]]

    def grav(self):
        return self.data[[x for x in self.columns if x.startswith('GRAVITY')]]

    def orient(self):
        return self.data[[x for x in self.columns if x.startswith('ORIENT')]]

    def atm_p(self):
        return self.data[[x for x in self.columns if x.startswith('ATMOSPHERIC PRESSURE')]]

    def loc_orient(self):
        return self.data[[x for x in self.columns if x.startswith('LOCATION ORIENTATION')]]

    __doc__ = """
        This Class Reads csv-style Sensordata created by AndroSensor and transforms it into a pandas DataFrame.
        Sensorvalues are available with their different methods.

        Gravity: estimated Gravity part of acceleration
        Acceleration: Total Acceleration felt by the Device
        Linear Acceleration: Linear Acceleration felt by the device
        """
