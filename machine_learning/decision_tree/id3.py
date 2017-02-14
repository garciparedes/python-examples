import pandas as pd
from machine_learning.utils.gainranking import GainRanking
from data_structures.labeled_tree import LabeledTree


class ID3:
    def __init__(self, training_set, class_name):
        self.class_name = class_name
        self.tree = self.generate_tree(training_set)
        print(self.tree)

        pass

    def generate_tree(self, training_set):

        return self.generate_sub_tree(training_set)

        pass

    def generate_sub_tree(self, data_pd):

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
                tree.add_child(v1, self.generate_sub_tree(d))

        return tree


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

    id3_tennis = ID3(data_pd, columns[-1])
