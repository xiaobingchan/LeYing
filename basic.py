#1，session的使用
import tensorflow as tf #引入TensorFlow库

m1 = tf.constant([[2, 2]])#定义一个一行两列的矩阵常量
m2 = tf.constant([[3],[3]])#定义一个两行一列的矩阵常量
dot_operation = tf.matmul(m1, m2)#定义m1和m2的TensorFlow矩阵乘法

# 使用会话的方法1
sess = tf.Session()#定义会话
result = sess.run(dot_operation)#执行会话乘法
#print(result)#打印矩阵相乘的结果
sess.close()#关闭会话

# 使用会话的方法2，会话简化达到相同效果
with tf.Session() as sess:
    result_ = sess.run(dot_operation)
    #print(result_)

#-----------------------------------------------
#2，占位符的使用
x1 = tf.placeholder(dtype=tf.float32, shape=None)
y1 = tf.placeholder(dtype=tf.float32, shape=None)
z1 = x1 + y1

x2 = tf.placeholder(dtype=tf.float32, shape=[2, 1])
y2 = tf.placeholder(dtype=tf.float32, shape=[1, 2])
z2 = tf.matmul(x2, y2)

with tf.Session() as sess:
    # when only one operation to run
    z1_value = sess.run(z1, feed_dict={x1: 1, y1: 2})

    # when run multiple operations
    z2_value = sess.run([z2],feed_dict={x2: [[2], [2]], y2: [[3, 3]]})
    #print(z1_value)
    #print(z2_value)

#-----------------------------------------------
#3，变量的使用
var = tf.Variable(0)    # our first variable in the "global_variable" set

add_operation = tf.add(var, 1)
update_operation = tf.assign(var, add_operation)

with tf.Session() as sess:
    # once define variables, you have to initialize them by doing this
    sess.run(tf.global_variables_initializer())
    for _ in range(3):
        sess.run(update_operation)
        print(sess.run(var))