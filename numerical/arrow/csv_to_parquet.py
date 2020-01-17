""" From: 'https://stackoverflow.com/a/45618618/3921457' """
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pathlib import Path

CSV_FILE_PATH = Path(__file__).parents[1] / 'data.csv'
PARQUET_FILE_PATH = Path(__file__).parents[1] / 'data.parquet'
CHUNK_SIZE = 100_000


def main():
    csv_stream = pd.read_csv(CSV_FILE_PATH, chunksize=CHUNK_SIZE, low_memory=False)

    chunk = next(csv_stream)
    parquet_schema = pa.Table.from_pandas(chunk).schema

    parquet_writer = pq.ParquetWriter(PARQUET_FILE_PATH, parquet_schema, compression='snappy')

    for i, chunk in enumerate(csv_stream):
        print("Chunk", i)
        table = pa.Table.from_pandas(chunk, parquet_schema)
        parquet_writer.write_table(table)

    parquet_writer.close()


if __name__ == '__main__':
    main()
