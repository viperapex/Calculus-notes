import tensorflow as tf

x = tf.constant(5.0)  # Note: constant, not Variable

with tf.GradientTape() as t:
    t.watch(x)  # Required here because x is a constant tensor
    y = x * x

dy_dx = t.gradient(y, x)
print(dy_dx)  # Output: tf.Tensor(6.0, shape=(), dtype=float32)
