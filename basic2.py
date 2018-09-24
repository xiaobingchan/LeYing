#-----------------------------------------------
#4，激活函数的使用
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# fake data
x = np.linspace(-5, 5, 200) #产生-5至5之间200个点
y_relu = tf.nn.relu(x)#定义relu激活函数，输入数据点
y_sigmoid = tf.nn.sigmoid(x)#定义sigmod激活函数，输入数据点
y_tanh = tf.nn.tanh(x)#定义tanh激活函数，输入数据点
y_softplus = tf.nn.softplus(x)#定义softplus，输入数据点
sess = tf.Session()#创建session
y_relu, y_sigmoid, y_tanh, y_softplus = sess.run([y_relu, y_sigmoid, y_tanh, y_softplus])#生成激活函数

#绘制relu的图像
plt.figure(1, figsize=(8, 6))
plt.subplot(221)
plt.plot(x, y_relu, c='red', label='relu')
plt.ylim((-1, 5))
plt.legend(loc='best')

#绘制sigmoid的图像
plt.subplot(222)
plt.plot(x, y_sigmoid, c='red', label='sigmoid')
plt.ylim((-0.2, 1.2))
plt.legend(loc='best')

#绘制tanh的图像
plt.subplot(223)
plt.plot(x, y_tanh, c='red', label='tanh')
plt.ylim((-1.2, 1.2))
plt.legend(loc='best')

#绘制softplus的图像
plt.subplot(224)
plt.plot(x, y_softplus, c='red', label='softplus')
plt.ylim((-0.2, 6))
plt.legend(loc='best')

plt.show()