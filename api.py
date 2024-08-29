from flask import Flask, render_template, request, redirect, url_for, flash, session, Response
import requests
from database.login import LoginMapper

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

@app.route("/video_feed")
def video_feed():
    def generate():
        r = requests.get('http://192.168.0.11:5000/video_feed', stream=True)
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                yield chunk
    return Response(generate(), content_type='multipart/x-mixed-replace; boundary=frame')

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
