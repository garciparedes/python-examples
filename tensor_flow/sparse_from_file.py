import tensorflow as tf

from data_sets.data_sets import DataSets


def main():
    data_set = DataSets.get_followers() - 1
    n = data_set.max(axis=0).max() + 1

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        print(sess.run(
            tf.scatter_nd(data_set.values.tolist(), data_set.shape[0] * [1.0],
                          [n, n])))


if __name__ == '__main__':
    main()
