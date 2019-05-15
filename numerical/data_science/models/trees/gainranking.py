import numpy as np
import pandas as pd
from numerical.data_science.res import DataSets


class GainRanking:
    """
    Class GainRanking
    """

    def __init__(self, data_input, class_name, debug=False):
        self.data = data_input
        self.class_name = class_name
        self.debug = debug
        self.h_S = self.entropy(self.data)
        self._gain_list = None

    @property
    def gain_list(self):
        if self._gain_list is None:
            columns = self.data.columns[self.data.columns != self.class_name]
            self._gain_list, self.data.ix[:, columns] = self.gain(self.data.ix[:, columns], self.h_S)
        return self._gain_list

    @property
    def gain_winner(self):
        return self.gain_list.idxmax(), self.data[self.gain_list.idxmax()]

    def gain(self, subdata, h_S):
        result = pd.Series(index=subdata.columns)
        for column in subdata.columns:
            a = self.sub_entropy(subdata[column])
            counts = subdata[column].value_counts()
            p = (counts / counts.sum())
            result[column] = (h_S - (p * a).sum())
        return result, subdata

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

    def __str__(self):
        return str(self.gain_list)


if __name__ == '__main__':
    data_pd = DataSets.get_weber_nominal()
    print(GainRanking(data_pd, data_pd.columns[-1]))
