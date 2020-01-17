import pandas as pd
from pathlib import Path


def main():
    file_path = Path('df.parquet')
    df = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [6, 7, 8, 9, 10]})
    df.to_parquet(file_path)

    df = pd.read_parquet(file_path)
    print(df)


if __name__ == '__main__':
    main()
