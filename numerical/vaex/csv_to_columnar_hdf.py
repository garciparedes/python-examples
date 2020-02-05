from shutil import rmtree

import pandas as pd

import vaex

from numerical.utils import (
    CSV_FILE_PATH,
    CHUNK_SIZE,
    COLUMNAR_HDF_FILE_PATH,
    TMP_PATH,
)


def main():
    print(f'HDF5 Stored Size: {CSV_FILE_PATH.stat().st_size / 1024 ** 3:.3f} GB')

    stream = pd.read_csv(
        CSV_FILE_PATH,
        chunksize=CHUNK_SIZE,
        low_memory=False,
        sep=',',
        encoding='latin-1',
    )
    TMP_PATH.mkdir(parents=True, exist_ok=True)
    for i, chunk in enumerate(stream):
        print(f'Processing {i + 1}-th chunk containing "{len(chunk)}" rows of data...')
        df_chunk = vaex.from_pandas(chunk, copy_index=False)
        export_path = TMP_PATH / f'part_{i}.hdf5'
        df_chunk.export_hdf5(str(export_path))

    df = vaex.open(str(TMP_PATH / 'part*'))

    df.export_hdf5(str(COLUMNAR_HDF_FILE_PATH))
    print(f'HDF5 Stored Size: {COLUMNAR_HDF_FILE_PATH.stat().st_size / 1024 ** 3:.3f} GB')

    rmtree(TMP_PATH)


if __name__ == '__main__':
    main()
