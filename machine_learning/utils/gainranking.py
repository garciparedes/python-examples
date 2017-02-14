import numpy as np
import pandas as pd


class GainRanking:
    """
    Class GainRanking
    """

    def __init__(self, data_input, class_name, debug=False):
        self.data = data_input
        self.class_name = class_name
        self.debug = debug
        self.h_S = self.class_entropy()
        self.gain_list = self.get_gain_list()

    def get_gain_list(self):
        columns = self.data.columns[self.data.columns != self.class_name]
        self.gain_list = self.gain(self.data[columns], self.h_S)
        return self.gain_list

    def get_gain_win(self):
        return self.gain_list.idxmax()

    def gain(self, subdata, h_S):
        result = pd.Series(index=subdata.columns)
        for column in subdata.columns:
            a = self.sub_entropy(subdata[column])
            counts = subdata[column].value_counts()
            p = (counts / counts.sum())
            result[column] = (h_S - (p * a).sum())
        return result

    def class_entropy(self):
        return self.entropy(self.data)

    def entropy(self, subdata):
        counts = subdata[self.class_name].value_counts()
        p = (counts / counts.sum())
        return (p * np.log2(1 / p)).sum()

    def sub_entropy(self, subdata):
        result = pd.Series(index=subdata.unique())
        cross = pd.concat([subdata, self.data[self.class_name]], axis=1)
        for cat in subdata.unique():
            result[cat] = self.entropy(cross[subdata == cat])
        return result


if __name__ == '__main__':
    outLook = pd.Series(["Sunny", "Overcast", "Rain"], dtype="category")
    temp = pd.Series(["Hot", "Mild", "Cold"], dtype="category")
    humidity = pd.Series(["High", "Normal"], dtype="category")
    wind = pd.Series(["Weak", "Strong"], dtype="category")
    playTennis = pd.Series(["Yes", "No"], dtype="category")

    columns = pd.Index(["Outlook", "Temperature", "Humidity", "Wind", "PlayTennis"])

    data = [
        [outLook[0], temp[0], humidity[0], wind[0], playTennis[1]],
        [outLook[0], temp[0], humidity[0], wind[1], playTennis[1]],
        [outLook[1], temp[0], humidity[0], wind[0], playTennis[0]],
        [outLook[2], temp[1], humidity[0], wind[0], playTennis[0]],
        [outLook[2], temp[2], humidity[1], wind[0], playTennis[0]],
        [outLook[2], temp[2], humidity[1], wind[1], playTennis[1]],
        [outLook[1], temp[2], humidity[1], wind[1], playTennis[0]],
        [outLook[0], temp[1], humidity[0], wind[0], playTennis[1]],
        [outLook[0], temp[2], humidity[1], wind[0], playTennis[0]],
        [outLook[2], temp[1], humidity[1], wind[0], playTennis[0]],
        [outLook[0], temp[1], humidity[1], wind[1], playTennis[0]],
        [outLook[1], temp[1], humidity[0], wind[1], playTennis[0]],
        [outLook[1], temp[0], humidity[1], wind[0], playTennis[0]],
        [outLook[2], temp[1], humidity[0], wind[1], playTennis[1]],
    ]

    data_pd = pd.DataFrame(data, columns=columns, dtype="category")

    tennis_gain = GainRanking(data_pd, columns[-1])
    print(tennis_gain.get_gain_list())