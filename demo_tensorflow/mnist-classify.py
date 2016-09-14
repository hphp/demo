import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./data/", one_hot=True)

#2, define model 
x = tf.placeholder(tf.float32, [None, 784]) #inputs of model
W = tf.Variable(tf.zeros([784, 10])) #weights
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)#output
y_ = tf.placeholder(tf.float32, [None, 10]) #labels

#3, define the loss and create a optimizer
cross_entropy = tf.reduce_mean(
        -tf.reduce_sum(y_ * tf.log(y), 
            reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

#4, define accuracy function
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#5, train the model
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    if i % 100 == 0:
        print("after %4d loop, achieved accuracy:%.4f" %(i,
            sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})))
