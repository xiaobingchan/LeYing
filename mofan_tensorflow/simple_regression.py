import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
x = np.linspace(-1, 1, 100)[:, np.newaxis] #创建一个新维度
noise = np.random.normal(0, 0.1, size=x.shape)#产生0-0.1之间x长度的随机数
y = np.power(x, 3) + noise#定义函数y为二次函数加上噪声的图像
plt.scatter(x, y)#定义x和y的散点图
plt.show()#画图


tf.set_random_seed(1)#设定随机种子
tf_x = tf.placeholder(tf.float32, x.shape) #定义占位符x
tf_y = tf.placeholder(tf.float32, y.shape) #定义占位符y
l1 = tf.layers.dense(tf_x, 10, tf.nn.relu)  #定义隐藏层，使用relu激活函数
output = tf.layers.dense(l1, 1)   #定义输出层
loss = tf.losses.mean_squared_error(tf_y, output)   # 定义损失值均方误差loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)#定义学习率为0.5的梯度下降算法的优化器
train_op = optimizer.minimize(loss)#执行
sess = tf.Session()         #定义会话
sess.run(tf.global_variables_initializer()) #会话占位符初始化

plt.ion()   # 打开交互模式

for step in range(500):
    #训练神经网络并输出损失值l和预测值pred
    _, l, pred = sess.run([train_op, loss, output], {tf_x: x, tf_y: y})
    if step % 20 == 0:#每训练5次输出一次
        # 画图
        plt.cla()
        plt.scatter(x, y)
        plt.plot(x, pred, 'r-', lw=5)#画出x和预测值pred的散点图
        plt.text(0.5, 0, 'Loss=%.4f' % l, fontdict={'size': 20, 'color': 'red'})#输出损失值l
        plt.pause(0.1)

plt.ioff()#关闭交互模式
plt.show()#画图