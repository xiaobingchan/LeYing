import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='test')
cur = conn.cursor()
# 查询
sql = "select * from info"
reCount = cur.execute(sql)  # 返回受影响的行数
print(reCount)
data = cur.fetchall()  # 返回数据,返回的是tuple类型
print(data)
cur.close()
conn.close()