import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_tp3",
)

dbcursor = mydb.cursor()

sql = "INSERT INTO klub (klub_nama) VALUES (%s)"
val = ("FC Barcelona",) 
dbcursor.execute(sql, val)
mydb.commit()
print(dbcursor.rowcount, "record inserted.")

dbcursor.execute("SELECT * FROM klub")
myresult=dbcursor.fetchall()
for x in myresult:
    print(x)

sql_delete = "DELETE FROM klub WHERE klub_nama = %s"
val_delete = ("FC Barcelona",)
dbcursor.execute(sql_delete, val_delete)
mydb.commit()
print(dbcursor.rowcount, "kategori deleted.")

print("\nSetelah delete :")
dbcursor.execute("SELECT * FROM klub")
myresult=dbcursor.fetchall()
for x in myresult:
    print(x)