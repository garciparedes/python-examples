#!/usr/bin/env python3


# EXAMPLE FROM: https://stackoverflow.com/a/43936905/3921457

import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import show, output_notebook, figure as bf



def main() -> None:
    df = pd.DataFrame({'S': [34,23, 12, 9],
                       'P':[65, 44, 81,23]})

    df_comb = df.join(df.divide(df.sum(axis=1), axis=0), rsuffix='_w').join(df.divide(df.sum(axis=1) * 2, axis=0), rsuffix='_w_labelheights')
    df_comb['P_w_labelheights'] += df_comb['S_w']
    df_comb

    f = bf()
    source = ColumnDataSource(df_comb)

    s = f.vbar(x='index', bottom=0, top='S_w', width=0.5, source=source)
    p = f.vbar(x='index', bottom='S_w', top=1, width=0.5, source=source, color='orange')

    s_label = f.text(x='index', y='S_w_labelheights', source=source, text='S')
    p_label = f.text(x='index', y='P_w_labelheights', source=source, text='P')

    show(f)


if __name__ == '__main__':
    main()
