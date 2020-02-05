from pathlib import Path

DIRECTORY_PATH = Path(__file__).parents[1]

CSV_FILE_PATH = DIRECTORY_PATH / 'data.csv'
PARQUET_FILE_PATH = DIRECTORY_PATH / 'data.parquet'
ARROW_FILE_PATH = DIRECTORY_PATH / 'data.arrow'
SQLITE_FILE_PATH = DIRECTORY_PATH / 'data.sqlite'
HDF_FILE_PATH = DIRECTORY_PATH / 'data.hdf5'
COLUMNAR_HDF_FILE_PATH = DIRECTORY_PATH / 'data-columnar.hdf5'

TMP_PATH = DIRECTORY_PATH / 'tmp'

CHUNK_SIZE = 100_000
TABLE_NAME = 'data'
