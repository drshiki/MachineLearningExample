import tensorflow as tf
import numpy as np

train_data = np.loadtxt("data/ex1data2.txt", delimiter=',')
X_train = np.float32(train_data[:,:train_data.shape[1]-1])
y_train = np.float32(train_data[:,-1]).reshape(train_data.shape[0],1)

X_mean = np.mean(X_train, axis=0)
X_devision = np.max(X_train, axis=0)-np.min(X_train, axis=0)
X_train = (X_train-np.mean(X_train, axis=0))/(np.max(X_train, axis=0)-np.min(X_train, axis=0))

W = tf.Variable(tf.zeros([X_train.shape[1],1]), dtype=tf.float32)
b = tf.Variable(0, dtype=tf.float32)

X = tf.placeholder(tf.float32, [X_train.shape[0], X_train.shape[1]])
y = tf.placeholder(tf.float32, [y_train.shape[0], 1])
print(X)

cost = 1.0/(2*y_train.shape[0])*tf.reduce_sum(tf.square(tf.subtract(tf.add(tf.matmul(X, W), b), y)))
init = tf.global_variables_initializer()
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

session = tf.Session()
session.run(init)

for i in range(5500):
    session.run(train, feed_dict={X:X_train, y: y_train})

print("w is :%s"%(session.run(W)))
print("b is :%.4f"%(session.run(b)))
print("cost is :%.4s"%(session.run(cost, feed_dict={X: X_train, y: y_train})))

