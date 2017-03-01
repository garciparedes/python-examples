import pandas as pd

from data_sets.data_sets import DataSets
from machine_learning.utils.gain_ranking_continous import GainRankingContinous
from machine_learning.decision_tree.id3 import ID3
from data_structures.labeled_tree import LabeledTree

class J48(ID3):
    def __init__(self, training_set, class_name):
        ID3.__init__(self, training_set, class_name, ranking=GainRankingContinous)


if __name__ == '__main__':
    data_pd_2 = DataSets.get_weather()
    j48_tennis = J48(data_pd_2, data_pd_2.columns[-1])
    print(j48_tennis)

