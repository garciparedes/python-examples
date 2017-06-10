import tensorflow as tf


def main():
    a_raw = [
        [0.0, 0.0, 1.0, 1.0],
        [1.0, 0.0, 0.0, 0.0],
        [1.0, 1.0, 0.0, 1.0],
        [1.0, 1.0, 0.0, 0.0]
    ]

    v_raw = [
        [0.25],
        [0.25],
        [0.25],
        [0.25]
    ]

    a = tf.Variable(a_raw, tf.float32)
    v = tf.Variable(v_raw, tf.float32)

    transition = tf.div(a, tf.reduce_sum(a, 0))
    page_rank = tf.matmul(transition, v)

    run_iteration = tf.assign(v, page_rank)

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)

        for step in range(7):
            print("Iteration: " + str(step))
            print(sess.run(run_iteration))

        tf.summary.FileWriter('logs/.', sess.graph)
        pass


if __name__ == '__main__':
    main()
