import numpy as np
import pandas as pd
from numerical.data_science.res import DataSets
from numerical.data_science import GainRanking


class GainRankingContinous(GainRanking):
    """
    Class GainRankingContinous
    """

    def __init__(self, data_input, class_name, debug=False):
        GainRanking.__init__(self, data_input, class_name, debug)

    def gain(self, subdata, h_S):
        result = pd.Series(index=subdata.columns)
        for column in subdata.columns:
            if subdata[column].dtype.name != 'category':
                if (subdata[column].dtype == np.int or
                            subdata[column].dtype == np.int16 or
                            subdata[column].dtype == np.int32 or
                            subdata[column].dtype == np.int64 or
                            subdata[column].dtype == np.int128):
                    subdata.ix[:, column] = self.discretize(subdata[column])
                else:
                    raise NotImplementedError

            a = self.sub_entropy(subdata[column])
            counts = subdata[column].value_counts()
            p = (counts / counts.sum())
            result[column] = (h_S - (p * a).sum())
        return result, subdata

    def discretize(self, subdata):
        new_data = pd.concat([subdata, self.data[self.class_name]], axis=1).sort_values(by=subdata.name)
        temp = new_data[self.class_name].iloc[0]
        i = 0
        cuts = []
        for current in new_data[self.class_name]:
            if temp != current:
                cuts.append((new_data[subdata.name].iloc[i] + new_data[subdata.name].iloc[i - 1]) / 2)
                temp = current
            i += 1
        alt = pd.DataFrame()
        for cut in cuts:
            alt = pd.concat([alt, subdata.apply(
                GainRankingContinous.discretize_split, 1, args=(cut,)).astype('category').rename(cut)], axis=1)
        return alt[self.gain(alt, self.h_S)[0].idxmax()]

    @staticmethod
    def discretize_split(value, point):
        if value < point:
            return ' < ' + str(point)
        else:
            return '>= ' + str(point)


if __name__ == '__main__':
    data_pd_2 = DataSets.get_weather_semi_nominal().ix[:, 1:]

    print(GainRankingContinous(data_pd_2, data_pd_2.columns[-1]))
