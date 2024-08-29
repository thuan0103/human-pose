import sqlite3

conn = sqlite3.connect("database/QLSV.db")

c = conn.cursor()

c.execute("DROP TABLE class_information")

conn.commit()
conn.close()