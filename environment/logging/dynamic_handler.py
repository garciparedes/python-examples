from io import StringIO

import logging


def main():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)  # "Necessary" condition.

    stream = StringIO()
    handler = logging.StreamHandler(stream)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger = logging.getLogger('example')

    logger.info('A info message.')
    logger.debug('A debug message.')

    # Starting loggable code...
    root.addHandler(handler)

    logger.info('Starting info message...')
    logger.debug('Starting debug message...')
    # loggable business logic...
    logger.info('Completed info message.')
    logger.debug('Completed debug message.')

    # Finishing loggable code...
    root.removeHandler(handler)
    handler.flush()

    logger.info('Another info message.')
    logger.debug('Another debug message.')

    # Handler results
    stream.seek(0)
    results = stream.readlines()
    results = [row.strip() for row in results]
    print(f'Handler results:\n{results}')


if __name__ == '__main__':
    main()
