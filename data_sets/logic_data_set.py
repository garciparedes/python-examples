import numpy as np
import pandas as pd
import string as st
from inspect import signature


class LogicDataSet():
    def __init__(self, logic_function):
        self.logic_function = logic_function
        self.num_vars = len(signature(self.logic_function).parameters)
        self._data = None
        pass

    @property
    def data(self):
        if self._data is None:
            self.generate_data()
        return self._data

    @property
    def data_as_pandas(self):
        return pd.DataFrame(self.data, columns=list(st.ascii_uppercase)[:self.num_vars] + ['Result'])

    @staticmethod
    def _array_logic_function(input_data, logic_f):
        input_data[-1] = logic_f(*input_data[:-1])
        return input_data

    def __str__(self):
        return str(self.data)

    def generate_data(self):
        self._data = np.zeros([2 ** self.num_vars, self.num_vars + 1], dtype=bool)
        for i in range(self.num_vars):
            self._data[:, i] = np.tile([0] * 2 ** i + [1] * 2 ** i, [2 ** (self.num_vars - i - 1)])
        self._data = np.apply_along_axis(LogicDataSet._array_logic_function, 1, self._data, self.logic_function)


def l(a, b, c, d, e):
    return bool(not (a and b) or not (c and d)) != bool(e)


if __name__ == '__main__':
    pd_l = LogicDataSet(l).data_as_pandas
    # pd_l.to_csv('logic_function.csv', index=False)
    print(pd_l)
