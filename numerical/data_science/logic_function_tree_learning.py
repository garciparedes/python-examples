from numerical.data_science.res import DataSets as ds
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier


def learn_function(a, b, c, d, e):
    return bool(not (a and b) or not (c and d)) != bool(e)


if __name__ == '__main__':
    np_data = ds.generate_from_logic_method(learn_function).data
    clf = tree.DecisionTreeClassifier()

    X_train, X_test, y_train, y_test = train_test_split(np_data[:,:-1],np_data[:,-1], test_size=0.33,
                                                        random_state=42)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
