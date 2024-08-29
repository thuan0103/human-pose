import sqlite3

conn = sqlite3.connect('database/QLSV.db')

c = conn.cursor()

many_customer = [
    (1,'DHIOT16B','Trần Minh Chính','A7.06'),
    (2,'DHTMDT16C','Nguyễn Minh Tuấn','D7.03'),
    (3,'DHIOT17B','Trần Minh Chính','A8.03')
    ]

#c.execute("INSERT INTO customers VALUES('John','Elder','john@codemy.com')")

c.executemany("INSERT INTO class_information VALUES (?,?,?,?)",many_customer)

conn.commit()
conn.close()