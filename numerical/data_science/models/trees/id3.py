from numerical.data_science.res import DataSets
from numerical.data_science import GainRanking
from utils.collections.labeled_tree import LabeledTree


class ID3:
    def __init__(self, training_set, class_name, ranking=GainRanking):
        self.class_name = class_name
        self.ranking = ranking
        self.tree = self.generate_tree(training_set)

    def generate_tree(self, data_pd):
        win, categories = self.ranking(data_pd, self.class_name).gain_winner
        tree = LabeledTree(win)
        for v1 in categories:
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

    def __str__(self):
        return str(self.tree)


if __name__ == '__main__':
    data_pd = DataSets.get_weber_nominal()
    id3_tennis = ID3(data_pd, data_pd.columns[-1])
    print(id3_tennis)

    '''
    pd_careval = DataSets.get_car_eval()
    id3_careval = ID3(pd_careval, pd_careval.columns[-1])
    print(id3_careval)
    '''

    pd_credit = DataSets.get_credit().ix[:, 1:]
    id3_credit = ID3(pd_credit, pd_credit.columns[0])
    print(id3_credit)
