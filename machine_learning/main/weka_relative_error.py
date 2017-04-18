#!/usr/bin/python3

import sys
import pandas as pd


if __name__ == "__main__":
    file_error = pd.read_csv(sys.argv[1])
    error_tase = float(sys.argv[2])
    error_count = (file_error['error'].abs() / file_error['actual'] <= error_tase).sum()
    print( error_count / float(file_error.shape[0]))
