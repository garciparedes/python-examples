class Tree(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def __str__(self):
        return self.str()

    def str(self, deep=1):

        str_out = str(self.data)

        for child in self.children:

            try:
                value = child.str(deep + 1)
            except AttributeError:
                value = child

            str_out += "\n" + deep * "\t" + " --> " + str(value)
        return str_out
