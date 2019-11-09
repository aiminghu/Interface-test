#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/8 0008 下午 16:32 
# @Author : aiminhu
# @File : conRedis.py 
# @Software: PyCharm
import redis
'''
第一步：导包
第二步：新建对象
第三布：实例化
第四步：调用
redis操作可参看：https://www.cnblogs.com/zhaohuhu/p/9140673.html
'''
#操作模式
# r = redis.Redis(host='127.0.0.1',port=6379)
# r.set('foo','Bar')
# print(r.get('foo'))

#连接池
'''
redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。
默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池
'''
pool = redis.ConnectionPool(host='127.0.0.1',port=6379)

r = redis.Redis(connection_pool=pool)
r.set('foo','bar')
print(r.get('foo'))