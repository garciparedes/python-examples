""" From: 'https://stackoverflow.com/a/45618618/3921457' """
import logging

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from numerical.utils.constants import (
    CSV_FILE_PATH,
    PARQUET_FILE_PATH,
    CHUNK_SIZE,
)

logger = logging.getLogger(__name__)


def csv_to_parquet():
    logger.info(f'Starting...')

    stream = pd.read_csv(
        CSV_FILE_PATH,
        chunksize=CHUNK_SIZE,
        low_memory=False,
        sep=',',
        encoding='latin-1',
    )

    logger.info(f'CSV Stored Size: {CSV_FILE_PATH.stat().st_size / 1024 ** 3:.3f} GB')

    chunk = next(stream)
    logger.debug(f'Processing 1-th chunk...')
    parquet_schema = pa.Table.from_pandas(chunk).schema
    parquet_writer = pq.ParquetWriter(PARQUET_FILE_PATH, parquet_schema, compression='snappy')

    for i, chunk in enumerate(stream, 2):
        logger.debug(f'Processing {i}-th chunk...')
        table = pa.Table.from_pandas(chunk, parquet_schema)
        parquet_writer.write_table(table)

    parquet_writer.close()

    logger.info(f'Parquet Stored Size: {PARQUET_FILE_PATH.stat().st_size / 1024 ** 3:.3f} GB')

    logger.info(f'Finished!')


def main():
    logging.basicConfig(level=logging.INFO)

    csv_to_parquet()


if __name__ == '__main__':
    main()
