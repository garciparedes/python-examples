import pandas as pd

from data_sets.data_sets import DataSets
from machine_learning.utils.gainranking import GainRanking
from data_structures.labeled_tree import LabeledTree


class ID3:
    def __init__(self, training_set, class_name):
        self.class_name = class_name
        self.tree = self.generate_tree(training_set)
        print(self.tree)

        pass

    def generate_tree(self, data_pd):

        tennis_gain = GainRanking(data_pd, self.class_name)
        win = tennis_gain.get_gain_win()

        tree = LabeledTree(win)

        for v1 in data_pd[win].unique():
            d = data_pd.ix[data_pd[win] == v1, data_pd.columns != win]

            if len(d[self.class_name].unique()) == 1:
                tree.add_child(v1, d[self.class_name].unique()[0])

            elif d.shape[1] == 1:
                tree.add_child(v1, " ".join(d[self.class_name].unique()))

            elif d.shape[0] == 0:
                tree.add_child(v1, None)

            else:
                tree.add_child(v1, self.generate_tree(d))

        return tree


if __name__ == '__main__':
    data_pd = DataSets.get_weber_nominal()
    id3_tennis = ID3(data_pd, data_pd.columns[-1])

    pd_careval = DataSets.get_car_eval()
    id3_careval = ID3(pd_careval, pd_careval.columns[-1])
