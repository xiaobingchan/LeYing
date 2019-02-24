# -*- coding:utf-8 -*-
from pymemcache.client.base import Client
client = Client(('localhost', 11211)) #连接memcached服务
client.set('some_key', 'some_value')  #设置键为some_key,值为some_value的哈希映射
result = client.get('some_key') #获取打印键为some_key的值
print(result)
