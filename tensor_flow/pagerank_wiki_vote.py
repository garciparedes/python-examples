import tensorflow as tf

from data_sets.data_sets import DataSets


def main():
    beta = 0.85
    steps = 20

    data_set = DataSets.get_wiki_vote() - 1
    n = data_set.max(axis=0).max() + 1

    a = tf.Variable(tf.transpose(
        tf.scatter_nd(data_set.values.tolist(), data_set.shape[0] * [1.0],
                      [n, n])),
                    tf.float32)

    v = tf.Variable(tf.fill([n, 1], tf.cast((1 / n), tf.float32)))

    o_degree = tf.reduce_sum(a, 0)

    condition = tf.not_equal(o_degree, 0)

    transition = tf.transpose(
        tf.where(condition,
                 tf.transpose(beta * tf.div(a, o_degree) + (1 - beta) / n),
                 tf.fill([n, n], tf.cast((1 / n), tf.float32))))

    page_rank = tf.matmul(transition, v, a_is_sparse=True)

    run_iteration = tf.assign(v, page_rank)

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)

        for step in range(steps):
            sess.run(run_iteration)

        print(sess.run(v))
        print(sess.run(tf.arg_max(v, dimension=0)))
        tf.summary.FileWriter('logs/.', sess.graph)
        pass


if __name__ == '__main__':
    main()
