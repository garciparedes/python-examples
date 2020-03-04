import pandas as pd


def main():
    base = pd.DataFrame({
        'value': ['hola', 'adios', 'lalala', 'hasta luego'],
        'flag': [False, True, True, True],
        'label': ['A', 'A', 'B', 'B']
    })
    base['value'] = base['value'].apply(lambda value: [value])
    base['index'] = base.index

    transformed = base.groupby('label').apply(lambda df: df['value'][df['flag']].cumsum()).reset_index()

    result = base.drop(columns={'value'}).merge(
        transformed.drop(columns={'label'}),
        left_on='index',
        right_on='level_1',
        how='left',
    )
    result = result.drop(columns={'index', 'level_1'})
    result['value'] = result['value'].apply(lambda value: value if isinstance(value, list) else [])
    print(result)


if __name__ == '__main__':
    main()
