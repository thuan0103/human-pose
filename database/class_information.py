import sqlite3

class Class_Information:
    def __init__(self, database_path = 'database/QLSV.db'):
        self.path = database_path
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def check_information(self, class_id=None, class_name=None, teacher=None, room_name=None):
        self.connect()
        
        sql_query = "SELECT * FROM class_information WHERE 1=1"
        conditions = []

        if class_id is not None:
            sql_query += " AND class_id =?"
            conditions.append(class_id)
        if class_name is not None:
            sql_query += " AND class_name =?"
            conditions.append(class_name)
        if teacher is not None:
            sql_query += " AND LOWER(teacher) = ?"
            conditions.append(teacher.lower())
        if room_name is not None:
            sql_query += " AND room_name = ?"
            conditions.append(room_name)

        self.cursor.execute(sql_query, tuple(conditions))
        class_inf = self.cursor.fetchall()
        text = "-----------Thông tin------------\n"

        for row in class_inf:
            try:
                cl_id, name, gv, room = row
                text += f"Tên phòng học {name}, tên giảng viên: {gv}, phòng học: {room}\n"
            except:
                text = False
                return text
        text += "-----------------------------"
        self.disconnect()
        return(text)
    
    def class_room(self):
        self.connect()
        self.cursor.execute("SELECT room_name FROM class_information")
        class_name = self.cursor.fetchall()
        dict = []
        for name in class_name:
            text = {"class_name": name[0]}
            dict.append(text)
        self.disconnect
        return dict

    def insert_information(self, class_name, teacher, room_name):
        self.connect()

        # Kiểm tra xem dữ liệu đã tồn tại chưa
        self.cursor.execute("""
            SELECT COUNT(*) FROM class_information
            WHERE class_name = ? AND teacher = ? AND room_name = ?
        """, (class_name, teacher, room_name))

        if self.cursor.fetchone()[0] == 0:
            # Chèn dữ liệu nếu chưa tồn tại
            self.cursor.execute("""
                INSERT INTO class_information (class_name, teacher, room_name)
                VALUES (?, ?, ?)
            """, (class_name, teacher, room_name))
            self.connection.commit()
            print("Data inserted successfully")
        else:
            print("Data already exists")

        self.disconnect()
if __name__ == "__main__":
    a = Class_Information()
    b = a.check_information(teacher="Trần Minh Chính")
    c = a.class_name()
    d = a.insert_information('DHIOT18C','Đinh Tiến Thuần','D7.04')
    print(c)

