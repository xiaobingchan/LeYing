import tensorflow as tf
import os
import datetime
starttime = datetime.datetime.now()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'#忽略cpu指令错误
a = tf.constant([1.0,2.0,3.0],name='input1')
b = tf.Variable(tf.random_uniform([3]),name='input2')
add = tf.add_n([a,b],name='addOP')
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter("D://TensorBoard//test",sess.graph)
    print(sess.run(add))
writer.close()

endtime = datetime.datetime.now()
#print((endtime - starttime).microseconds)#统计程序运行时间
print(tf.__path__);