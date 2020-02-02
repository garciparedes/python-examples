from pathlib import Path

DIRECTORY_PATH = Path(__file__).parents[1]

CSV_FILE_PATH = DIRECTORY_PATH / 'data.csv'
PARQUET_FILE_PATH = DIRECTORY_PATH / 'data.parquet'
SQLITE_FILE_PATH = DIRECTORY_PATH / 'data.sqlite'
HDF_FILE_PATH = DIRECTORY_PATH / 'data.hdf5'

CHUNK_SIZE = 100_000
TABLE_NAME = 'data'
