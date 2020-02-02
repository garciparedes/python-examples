import logging

import modin.pandas as pd
from ..utils import (
    PARQUET_FILE_PATH,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info(f'Starting...')

    logger.info(f'Parquet Stored Size: {PARQUET_FILE_PATH.stat().st_size / 1024 ** 3:.3f} GB')

    df = pd.read_parquet(PARQUET_FILE_PATH)
    logger.info(f'In memory Size: {df.memory_usage(deep=True).sum() / 1024 ** 3:.3f} GB')

    logger.info(f'Finished!')


if __name__ == '__main__':
    main()
