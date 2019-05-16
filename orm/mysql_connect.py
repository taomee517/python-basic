import mysql.connector

# conn = mysql.connector.connect(user='root', password='fastgo123',
# database='db_terminal', host="192.168.6.160", port=3306)
conn = mysql.connector.connect(user='root', password='lt030517', database='lifevc', host="127.0.0.1", port=3306)
print(conn)
cursor = conn.cursor()
# cursor.execute('select imei from tb_terminal where id = 47 ')
cursor.execute('select * from tb_user')
values = cursor.fetchall()
# print(values)
for t in values:
    print(t)
cursor.close()
conn.close()
