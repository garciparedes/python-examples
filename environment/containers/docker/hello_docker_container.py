from datetime import datetime

import docker


def main():
    start = datetime.now()

    client = docker.from_env()

    apt_dependencies = ' '.join([
        'vim',
    ])

    pip_dependencies = ' '.join([
        'numpy',
        'pandas',
    ])

    code = ';'.join([
        'import numpy as np',
        'size = 100',
        'random_numbers = np.random.uniform(size=size)',
        'print(random_numbers)'
    ])

    container = client.containers.run("python", 'tail -f /dev/null', detach=True)
    result = container.exec_run(f"apt-get update")
    print(result.output.decode())

    result = container.exec_run(f"apt-get install -y {apt_dependencies}")
    print(result.output.decode())

    result = container.exec_run(f"pip install {pip_dependencies}")
    print(result.output.decode())

    result = container.exec_run(f"python -c '{code}'")
    print(result.output.decode())

    container.stop()
    end = datetime.now()

    print(f'Elapsed Time: {end - start}')

if __name__ == '__main__':
    main()
