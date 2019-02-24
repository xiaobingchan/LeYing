import ibm_db
conn = ibm_db.connect("DATABASE=test;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2admin;PWD=a12345678;", "", "")
if conn:
    print('已链接DB2');