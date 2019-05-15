from numerical import tensorflow as tf


def main():
    a_raw = [
        [0.0, 0.0, 1.0, 1.0],
        [1.0, 0.0, 0.0, 0.0],
        [1.0, 1.0, 0.0, 1.0],
        [1.0, 1.0, 0.0, 0.0]
    ]
    beta = 0.85
    steps = 7

    a = tf.Variable(a_raw, tf.float32)
    n = int(a.get_shape()[0])

    v = tf.Variable(tf.fill([n, 1], 1 / n), tf.float32)

    o_degree = tf.reduce_sum(a, 0)

    condition = tf.not_equal(o_degree, 0)

    transition = tf.transpose(
        tf.where(condition,
                 tf.transpose(beta * tf.div(a, o_degree) + (1 - beta) / n),
                 tf.fill([n, n], 1 / n)))

    page_rank = tf.matmul(transition, v)

    run_iteration = tf.assign(v, page_rank)

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        print(sess.run(transition))

        for step in range(steps):
            sess.run(run_iteration)

        print(sess.run(v))

        tf.summary.FileWriter('logs/.', sess.graph)
        pass


if __name__ == '__main__':
    main()
