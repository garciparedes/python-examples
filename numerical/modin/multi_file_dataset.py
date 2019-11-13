from datetime import datetime
from pathlib import Path

import modin.pandas as pd


def main():
    directory_path = Path('data/')
    pattern = '*.csv'

    start = datetime.now()

    df = pd.concat(
        (file_to_dataframe(file_path) for file_path in directory_path.glob(pattern)),
        sort=False,
        copy=False,
    )

    end = datetime.now()

    print(f'Units mean: "{df["KWMENG_C"].mean()}"')
    print(f'Elapsed "{end - start}" seconds')


def file_to_dataframe(file_path: Path) -> pd.DataFrame:
    print(f'Reading "{file_path}"...')
    return pd.read_csv(file_path, sep='|', decimal=',', encoding='latin-1')


if __name__ == '__main__':
    main()
