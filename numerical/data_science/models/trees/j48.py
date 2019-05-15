from numerical.data_science.res import DataSets
from numerical.data_science import GainRankingContinous
from numerical.data_science import ID3


class J48(ID3):
    def __init__(self, training_set, class_name):
        ID3.__init__(self, training_set, class_name, ranking=GainRankingContinous)


if __name__ == '__main__':
    data_pd_2 = DataSets.get_weather()
    j48_tennis = J48(data_pd_2, data_pd_2.columns[-1])
    print(j48_tennis)

