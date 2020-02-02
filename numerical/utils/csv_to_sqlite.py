import logging
import sqlite3
import pandas as pd

from numerical.utils.constants import (
    CSV_FILE_PATH,
    SQLITE_FILE_PATH,
    CHUNK_SIZE,
    TABLE_NAME
)

logger = logging.getLogger(__name__)


def csv_to_sqlite():
    logger.info(f'Starting...')

    logger.info(f'CSV Stored Size: {CSV_FILE_PATH.stat().st_size / 1024 ** 3:.3f} GB')

    connection = sqlite3.connect(SQLITE_FILE_PATH)

    logger.info(f'Dropping "{TABLE_NAME}" table...')
    connection.execute(f'DROP TABLE IF EXISTS {TABLE_NAME};')

    stream = pd.read_csv(
        CSV_FILE_PATH,
        chunksize=CHUNK_SIZE,
        low_memory=False,
        sep=',',
        encoding='latin-1',
    )
    for i, chunk in enumerate(stream, 1):
        logger.info(f'{i}-th iteration\tInserting "{len(chunk)}" rows on "{TABLE_NAME}"...')
        chunk.to_sql(TABLE_NAME, connection, if_exists='append', chunksize=10_000)


    logger.info(f'SQLITE Stored Size: {SQLITE_FILE_PATH.stat().st_size / 1024 ** 3:.3f} GB')

    logger.info(f'Finished!')


def main():
    logging.basicConfig(level=logging.INFO)
    csv_to_sqlite()


if __name__ == '__main__':
    main()
