import pymssql

conn = pymssql.connect(host='JCVECB54U9LXMZQ\SQLEXPRESSLYJ',
                       user='sa',
                       password='a12345678',
                       database='test',
                       charset='utf8')

#查看连接是否成功
cursor = conn.cursor()
try:
   sql = "insert into student values(1, '张三')"
   cursor.execute(sql)
   conn.commit()
except Exception as ex:
   conn.rollback()
   raise ex
finally:
   sql = "select * from student"
   cursor.execute(sql)
   #用一个rs变量获取数据
   rs = cursor.fetchall()
   print(rs)