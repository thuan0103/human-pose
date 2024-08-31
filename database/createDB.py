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
# c.execute("""
#     CREATE TABLE  class_information(
#             class_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             class_name TEXT NOT NULL,
#             teacher TEXT NOT NULL,
#             room_name TEXT NOT NULL
#           )
# """)
# c.execute("""
#     CREATE TABLE  camera(
#             camera_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             class_id INTEGER,
#             camera TEXT NOT NULL,
#             FOREIGN KEY (class_id) REFERENCES class_information(class_id)
#           )
# """)

c.execute("""
    CREATE TABLE students(
            students_id TEXT PRIMARY KEY,
            class_id INTEGER,
            action NOT NULL,
            FOREIGN KEY (class_id) REFERENCES class_information(class_id)
          )
""")
conn.commit()
conn.close()