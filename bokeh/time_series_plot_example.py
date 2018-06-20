#!/usr/bin/env python3


# EXAMPLE FROM: https://stackoverflow.com/a/45984782/3921457


import pandas as pd

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show


def main() -> None:
    dic = {
        '2017-08-11': {'Yes': 157, 'Not sure': 2, 'No': 1},
        '2017-08-22': {'Yes': 142, 'Not sure': 12},
        '2017-08-01': {'Yes': 112, 'Others': 10, 'Not sure': 4, 'No': 9},
        '2017-08-17': {'Yes': 117, 'No': 12, 'Not sure': 11, 'Others': 2},
        '2017-08-25': {'Yes': 61, 'Not sure': 9},
        '2017-08-23': {'Yes': 268, 'Not sure': 20, 'No': 1},
        '2017-07-10': {'Yes': 123, 'Not sure': 4, 'No': 1},
        '2017-08-10': {'Yes': 343, 'Not sure': 20},
        '2017-07-13': {'Yes': 116, 'Others': 1, 'Not sure': 14, 'No': 2},
        '2017-07-14': {'Yes': 255, 'Not sure': 22, 'No': 6},
        '2017-08-07': {'Yes': 73, 'Others': 3, 'Not sure': 4, 'No': 5},
        '2017-08-04': {'Not sure': 11, 'Others': 8, 'Yes': 178, 'No': 10},
        '2017-08-16': {'Not sure': 10, 'Yes': 219},
        '2017-07-18': {'Yes': 1, 'No': 1},
        '2017-08-15': {'Yes': 301, 'Others': 4, 'Not sure': 37, 'No': 31},
        '2017-08-08': {'Yes': 38, 'No': 2, 'Others': 1},
        '2017-08-09': {'Yes': 120, 'Not sure': 3},
        '2017-08-28': {'Yes': 206, 'Others': 2, 'Not sure': 18, 'No': 24},
        '2017-08-14': {'Yes': 46, 'No': 3, 'Not sure': 5, 'Others': 7}
    }

    df = pd.DataFrame.from_dict(dic, orient="index")
    df = df.fillna(0)
    df.index = pd.to_datetime(df.index)
    df.index.name = 'Date'
    df.sort_index(inplace=True)

    df['Total'] = df.Yes + df['Not sure'] + df.No + df.Others
    df['Precision'] = round(df.Yes/df.Total, 2)
    df
    source = ColumnDataSource(df)

    p = figure(x_axis_type="datetime", plot_width=800, plot_height=350)
    p.line('Date', 'Precision', source=source)

    show(p)


if __name__ == '__main__':
    main()
