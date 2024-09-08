from flask import Flask, render_template, request, redirect, url_for, flash, session, Response, jsonify, request
import requests
import sys
sys.path.append('.')
from database.login import LoginMapper
from database.class_information import Class_Information
app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route("/favicon.ico")
def favicon():
    return '', 204

@app.route("/sign")
def sign():
    return render_template("login.html")

@app.route("/search")
def search():
    return render_template("index.html")

@app.route("/video_feed/<class_name>")
def video_feed(class_name):
    def generate():
        video_feed_url = f'http://192.168.88.225:5000/video_feed/{class_name}'
        try:
            r = requests.get(video_feed_url, stream=True)
            if r.status_code == 200:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        yield chunk
            else:
                yield b'Error: Camera not available'
        except requests.RequestException:
            yield b'Error: Camera not available'

    return Response(generate(), content_type='multipart/x-mixed-replace; boundary=frame')


@app.route("/api/classes", methods=['GET'])
def get_classes():
    path = 'database/QLSV.db'
    class_db = Class_Information()
    classes = class_db.class_room()
    return jsonify(classes)

@app.route("/api/add_class", methods=['POST'])
def add_class():
    add_class = request.get_json()
    class_name = add_class['class_name']
    teacher = add_class['instructor']
    room_name = add_class['room']
    class_inf = Class_Information()
    insert = class_inf.insert_information(class_name=class_name,teacher=teacher,room_name=room_name)
    return jsonify(add_class)

@app.route("/login", methods=["POST"])
def logins():
    username = request.form.get("username")
    password = request.form.get("password")
    path = 'database/QLSV.db'
    login_db = LoginMapper(path)
    select = login_db.select_information(username, password)
    if select:
        flash('Đăng nhập thành công', 'login')
        return redirect(url_for("search"))
    else:
        flash('Sai tài khoản hoặc mật khẩu', 'login')
        return redirect(url_for("sign"))

@app.route("/register", methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    path = 'database/QLSV.db'
    login_db = LoginMapper(path)
    insert_db = login_db.insert_information(username, password, email)
    if insert_db:
        flash('Đăng ký thành công', 'register')
    else:
        flash('Tài khoản đã tồn tại', 'register')
        return redirect(url_for("sign"))
    return redirect(url_for("sign"))

@app.route('/clear_flash')
def clear_flash():
    session.pop('_flashes', None)  # Xóa các thông báo flash trong session
    return redirect(url_for('sign'))

if __name__ == "__main__":
    app.run(debug=True)
