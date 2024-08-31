import sqlite3

conn = sqlite3.connect("database/QLSV.db")

c = conn.cursor()

c.execute("DROP TABLE camera")

conn.commit()
conn.close()