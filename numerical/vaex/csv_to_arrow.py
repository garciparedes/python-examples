import logging

import vaex

from numerical.utils.constants import (
    CSV_FILE_PATH,
    ARROW_FILE_PATH,
    HDF_FILE_PATH,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info(f'Starting...')

    logger.info(f'CSV Stored Size: {CSV_FILE_PATH.stat().st_size / 1024 ** 3:.3f} GB')

    df = vaex.open(str(CSV_FILE_PATH), convert=str(HDF_FILE_PATH))
    logger.info(f'HDF5 Stored Size: {HDF_FILE_PATH.stat().st_size / 1024 ** 3:.3f} GB')

    df.export(str(ARROW_FILE_PATH))
    logger.info(f'ARROW Stored Size: {ARROW_FILE_PATH.stat().st_size / 1024 ** 3:.3f} GB')

    logger.info(f'Finished!')


if __name__ == '__main__':
    main()
