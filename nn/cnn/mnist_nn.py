from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

# one layer neural network, 92% accurency
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
logits = tf.matmul(x, W)+b
#y = tf.nn.softmax(tf.matmul(w, x)+b)
y_ = tf.placeholder(tf.float32, [None, 10])
#cross_entropy = tf.reduce_mean(tf.reduce_sum(-y_*tf.log(y), reduction_indices=[1]))
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=logits))
train = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(64)
    sess.run(train, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(y_, 1))
acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
acc_v = sess.run(acc, feed_dict={x:mnist.test.images, y_:mnist.test.labels})
print(":D accurency = %f"%acc_v)