from collections import UserDict


class OscarDict(UserDict):

    def __getitem__(self, key):
        value = self.data[key]
        if callable(value):
            value = value()
            self.data[key] = value
        return value


def main():
    base = {'a': 3, 'b': lambda: 'Oscar'}
    fancy = OscarDict(base)

    print(fancy['a'])
    print(fancy['b'])

    fancy['c'] = lambda: 'Sergio'

    print(fancy['c'])


if __name__ == '__main__':
    main()
