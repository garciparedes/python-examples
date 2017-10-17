#! /usr/bin/python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats

def main():

    t1 = np.array(['1.1','1.2','1.3','1.4','1.5',
                   '1.6', '1.7', '1.8', '1.9', '1.10',
                   '1.11', '1.12', '1.13', '1.15', '1.16',
                   '1.17', '1.18', '1.19', '1.20'])

    t2 = np.array(['1.14', '1.21', '1.22', '1.23', '1.24',
                   '1.25', '1.26', '1.27', '1.28', '1.29',
                   '1.31', '1.32'])

    t3 = np.array(['2.1','2.2','2.3','2.4','2.6',
                   '2.7','2.8','2.9','2.13','2.18',
                   '2.19','2.21','2.22','2.23','2.24',
                   '2.25','2.35'])

    exercises = pd.DataFrame([t1,t2,t3]).T
    #print(exercises)

    p_i = np.full(3, exercises.shape[1])    
    #p_i = exercises.count(axis=0)

    p_i_normalized = p_i / np.sum(p_i)

    t_rand = np.argmax(np.random.multinomial(1, p_i_normalized))

    e_rand = (np.random.randint(0, p_i[t_rand]))

    print(exercises.iloc[e_rand, t_rand])


if __name__ == '__main__':
    main()
