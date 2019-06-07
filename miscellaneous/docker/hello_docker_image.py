from io import StringIO, BytesIO
from datetime import datetime

import docker


def main():

    client = docker.from_env()

    apt_dependencies = ' '.join([
        'vim',
    ])

    pip_dependencies = ' '.join([
        'numpy',
    ])

    code = ';'.join([
        'import numpy as np',
        'size = 100',
        'random_numbers = np.random.uniform(size=size)',
        'print(random_numbers)'
    ])

    version = 'latest'
    tag = 'hello-docker-py'

    output = BytesIO('\n'.join([
        f'FROM python:{version}',
        f'RUN apt-get update && apt-get install -y {apt_dependencies}',
        f'RUN pip install {pip_dependencies}',
    ]).encode())
    client.images.build(fileobj=output, tag=tag)

    start = datetime.now()

    container = client.containers.run(tag, 'tail -f /dev/null', detach=True)

    result = container.exec_run(f"python -c '{code}'")
    print(result.output.decode())

    result = container.exec_run(f"python -c '{code}'")
    print(result.output.decode())

    end = datetime.now()

    print(f'Elapsed Time: {end - start}')
    container.stop()


if __name__ == '__main__':
    main()
