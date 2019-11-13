import modin.pandas as pd
import numpy as np


def main():
    frame_data = np.random.randint(0, 100, size=(2 ** 10, 2 ** 8))
    df = pd.DataFrame(frame_data)
    print(df.mean())


if __name__ == '__main__':
    main()
