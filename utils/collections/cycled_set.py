from collections.abc import MutableSet


class CycledSet(MutableSet):
    def __init__(self, iterable=()):
        self.data = set(iterable)

    def __contains__(self, value):
        return value in self.data

    def __iter__(self):
        while True:
            if any(self.data):
                yield from self._iter_data()
            else:
                yield None

    def _iter_data(self):
        copied_data = set(self.data)
        for element in copied_data:
            if element not in self.data:
                continue
            yield element

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)

    def add(self, item):
        self.data.add(item)

    def discard(self, item):
        self.data.discard(item)
