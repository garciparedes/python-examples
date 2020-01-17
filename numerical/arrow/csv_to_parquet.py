""" From: 'https://stackoverflow.com/a/45618618/3921457' """
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pathlib import Path

csv_file = Path('df.csv')
parquet_file = Path('df.parquet')
CHUNK_SIZE = 1


def main():
    csv_stream = pd.read_csv(csv_file, chunksize=CHUNK_SIZE, low_memory=False)

    chunk = next(csv_stream)
    parquet_schema = pa.Table.from_pandas(chunk).schema

    parquet_writer = pq.ParquetWriter(parquet_file, parquet_schema, compression='snappy')

    for i, chunk in enumerate(csv_stream):
        print("Chunk", i)
        table = pa.Table.from_pandas(chunk, parquet_schema)
        parquet_writer.write_table(table)

    parquet_writer.close()


if __name__ == '__main__':
    main()
