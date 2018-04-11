import mysql.connector

conn = mysql.connector.connect(user='root', password='root', host='localhost', database='bortec_inv_system_db')
cursor = conn.cursor()
cursor.execute('select * from inventory_stocks')
print(cursor.fetchall())
