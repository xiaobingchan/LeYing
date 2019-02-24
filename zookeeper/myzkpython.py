# -*- coding: utf-8 -*-
from kazoo.client import KazooClient
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
zk.ensure_path('/mysql/test')
##zk.create('/mysql/test/node',b'node value')
if zk.exists("/mysql/test"):
    print(zk.get_children('/mysql/test'))
    print(zk.get('/mysql/test/node'))
else:
    zk.create('/mysql/test/node', b'node value')