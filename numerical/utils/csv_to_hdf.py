import logging
import pandas as pd

from numerical.utils.constants import (
    CSV_FILE_PATH,
    HDF_FILE_PATH,
    CHUNK_SIZE,
    TABLE_NAME,
)

logger = logging.getLogger(__name__)


def csv_to_hdf():
    logger.info(f'Starting...')

    logger.info(f'CSV Stored Size: {CSV_FILE_PATH.stat().st_size / 1024 ** 3:.3f} GB')

    if HDF_FILE_PATH.exists():
        HDF_FILE_PATH.unlink()

    stream = pd.read_csv(
        CSV_FILE_PATH,
        chunksize=CHUNK_SIZE,
        low_memory=False,
        sep=',',
        encoding='latin-1',
    )
    for i, chunk in enumerate(stream, 1):
        print(f'{i}-th iteration\tInserting "{len(chunk)}" rows on "{TABLE_NAME}"...')
        chunk.to_hdf(HDF_FILE_PATH, TABLE_NAME)

    logger.info(f'HDF Stored Size: {HDF_FILE_PATH.stat().st_size / 1024 ** 3:.3f} GB')

    logger.info(f'Finished!')


def main():
    logging.basicConfig(level=logging.INFO)

    csv_to_hdf()


if __name__ == '__main__':
    main()
