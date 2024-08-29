import sqlite3

conn = sqlite3.connect('database/QLSV.db')

c = conn.cursor()


# c.execute("""
#         CREATE TABLE login (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT NOT NULL UNIQUE,
#             password TEXT NOT NULL,
#             email TEXT
#           )
# """)
c.execute("""
    CREATE TABLE  class_information(
            class_id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name TEXT NOT NULL,
            teacher TEXT NOT NULL,
            room_name TEXT NOT NULL
          )
""")
conn.commit()
conn.close()