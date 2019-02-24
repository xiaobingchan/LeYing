#session的使用，介绍两种启动Session的方式，进行矩阵乘法运算
import tensorflow as tf #引入TensorFlow库

m1 = tf.constant([[2,2],[3,4]])#定义一个一行两列的矩阵常量
m2 = tf.constant([[3,4],[3,1]])#定义一个两行一列的矩阵常量
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
#占位符的使用
x1 = tf.placeholder(dtype=tf.float32, shape=None)#用占位符定义常量x1
y1 = tf.placeholder(dtype=tf.float32, shape=None)#用占位符定义常量y1
z1 = x1 + y1#定义z2为x1和y1相加的结果

x2 = tf.placeholder(dtype=tf.float32, shape=[2, 1])#用占位符定义2行1列矩阵x2
y2 = tf.placeholder(dtype=tf.float32, shape=[1, 2])#用占位符定义1行2列矩阵y2
z2 = tf.matmul(x2, y2)#定义z2为x2和y2矩阵相乘的结果

with tf.Session() as sess:
    #将常量放入占位符
    z1_value = sess.run(z1, feed_dict={x1: 1, y1: 2})

    # 将矩阵放入占位符
    z2_value = sess.run([z2],feed_dict={x2: [[2], [2]], y2: [[3, 3]]})
    print(z1_value)
    print(z2_value)

#-----------------------------------------------
#变量的使用
var = tf.Variable(0)#定义一个常量var，数值为0

add_operation = tf.add(var, 1)#定义一个常量加法运算，var数值加1
update_operation = tf.assign(var, add_operation)#将加法运算

with tf.Session() as sess:#开启会话
    sess.run(tf.global_variables_initializer())#变量本地初始化
    for _ in range(3):#运算循环3次
        sess.run(update_operation)#执行加法运算
        print(sess.run(var))#输出每次的运算结果

