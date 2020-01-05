import os
import logging

from typing import List
from io import StringIO

logger = logging.getLogger(__name__)


class DynamicHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__(stream=StringIO())
        self.level = logging.INFO
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def activate(self, target: logging.Logger = logging.getLogger()) -> None:
        target.setLevel(logging.DEBUG)  # "Necessary" condition.
        target.addHandler(self)

    def deactivate(self, target: logging.Logger = logging.getLogger()) -> None:
        target.removeHandler(self)
        self.flush()

    @property
    def rows(self) -> List[str]:
        stream = self.stream
        stream.seek(os.SEEK_SET)
        results = stream.readlines()
        stream.seek(os.SEEK_END)
        results = [row.strip() for row in results]
        return results


def function():
    logger.info('Starting info message...')
    logger.debug('Starting debug message...')
    # loggable business logic...
    logger.info('Completed info message.')
    logger.debug('Completed debug message.')


def main():
    handler = DynamicHandler()

    logger.info('A info message.')
    logger.debug('A debug message.')

    handler.activate()
    function()
    handler.deactivate()

    logger.info('Another info message.')
    logger.debug('Another debug message.')

    print(f'Handler results:\n{handler.rows}')


if __name__ == '__main__':
    main()
