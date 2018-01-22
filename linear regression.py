import tensorflow as tf
import numpy as np

# load data
train_data = np.loadtxt("data/ex1data1.txt", delimiter=",")

# split data
X_train = np.float32(train_data[:,0])
y_train = np.float32(train_data[:,1])

# declare parameters
w = tf.Variable(0, dtype=tf.float32)
b = tf.Variable(0, dtype=tf.float32)

X = tf.placeholder(tf.float32, X_train.shape[0])
y = tf.placeholder(tf.float32, y_train.shape[0])

cost = 1.0/(2*y_train.shape[0])*tf.reduce_sum((X*w+b-y)**2)

init = tf.global_variables_initializer()
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
session = tf.Session()
session.run(init)
print("cost is ",session.run(cost, feed_dict={X: X_train, y: y_train}))

for i in range(1500):
    session.run(train, feed_dict={X: X_train, y: y_train})
    if i % 100 == 0:
        print("cost is :",session.run(cost, feed_dict={X: X_train, y: y_train}))

print("w is :%.4f"%(session.run(w)))
print("b is :%.4f"%(session.run(b)))
print("cost is :%.4f"%(session.run(cost, feed_dict={X: X_train, y: y_train})))
