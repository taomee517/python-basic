import mysql.connector

conn = mysql.connector.connect(user='root', password='fastgo123', database='db_terminal', host="192.168.6.160", port=3306)
print(conn)
cursor = conn.cursor()
cursor.execute('select imei from tb_terminal where id = 47 ')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
