import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students")

conn.commit()
conn.close()

print("Students table deleted")