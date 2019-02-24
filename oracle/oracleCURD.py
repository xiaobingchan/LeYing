import cx_Oracle
conn=cx_Oracle.connect('luyanjie2/a12345678@orcl')
c=conn.cursor()
c.execute("create table python_curd(id number, name varchar2(50),password varchar(50),primary key(id))")
conn.commit();
c.close()
conn.close()