class LabeledTree(object):
    def __init__(self, data):
        self.data = data
        self.children = {}

    def add_child(self, label, obj):
        self.children[label] = obj

    def __str__(self):
        return self.str()

    def str(self, deep=1):

        str_out = str(self.data)

        for key, value in self.children.items():

            try:
                value = value.str(deep + 1)
            except AttributeError:
                value = value

            str_out += "\n" + deep * "\t" + str(key) + " --> " + str(value)
        return str_out
