import psycopg2
# psql -p 5433 -U postgres -d postgres
# psql --version

# 创建连接对象
conn = psycopg2.connect(database="postgres", user="postgres", password="a12345678", host="localhost", port="5433")
cur = conn.cursor()  # 创建指针对象

# 创建表
cur.execute("CREATE TABLE student(id integer,name varchar,sex varchar);")

# 插入数据
cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s)", (1, 'Aspirin', 'M'))
# 关闭练级
conn.commit()

# 获取结果
cur.execute('SELECT * FROM student')
results = cur.fetchall()
print(results)

cur.close()
conn.close()
