class LabeledTree(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, label, obj):
        self.children.append((label, obj))

    def __str__(self):
        return self.str()

    def str(self, deep=1):

        str_out = str(self.data)

        for child in self.children:

            try:
                value = child[1].str(deep + 1)
            except AttributeError:
                value = child[1]

            str_out += "\n" + deep * "\t" + str(child[0]) + " --> " + str(value)
        return str_out
