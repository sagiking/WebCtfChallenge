from flask import Flask, render_template, request, url_for
import sqlite3
import os

if not os.path.exists("./logon.db"):
    conn = sqlite3.connect("./logon.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pass_table (
        username text,
        password text,
        id text,
        priv text
    )
    """)

    conn.commit()

    cursor.execute("INSERT INTO pass_table (username, password, id, priv) VALUES (?, ?, ?, ?)", ("flag_user", "flag{W38_A77ACK5_@R3_C00L}", "39571963", "Critical"))
    cursor.execute("INSERT INTO pass_table (username, password, id, priv) VALUES (?, ?, ?, ?)", ("superuser", "secretpassword123", "80650170", "high"))
    cursor.execute("INSERT INTO pass_table (username, password, id, priv) VALUES (?, ?, ?, ?)", ("systemuser", "sys8642$!!", "79581677", "high"))
    cursor.execute("INSERT INTO pass_table (username, password, id, priv) VALUES (?, ?, ?, ?)", ("adminhacker", "administrator", "69067261", "medium"))
    cursor.execute("INSERT INTO pass_table (username, password, id, priv) VALUES (?, ?, ?, ?)", ("DBuser", "p@55w0rd1!", "27498925", "medium"))
    cursor.execute("INSERT INTO pass_table (username, password, id, priv) VALUES (?, ?, ?, ?)", ("admin", "admin", "49601703", "medium"))
    cursor.execute("INSERT INTO pass_table (username, password, id, priv) VALUES (?, ?, ?, ?)", ("webuser", "qwert12345", "76336573", "medium"))
    cursor.execute("INSERT INTO pass_table (username, password, id, priv) VALUES (?, ?, ?, ?)", ("management", "hackercommunity1", "82341299", "low"))
    cursor.execute("INSERT INTO pass_table (username, password, id, priv) VALUES (?, ?, ?, ?)", ("weak_user", "noobuser2", "25900108", "low"))
    cursor.execute("INSERT INTO pass_table (username, password, id, priv) VALUES (?, ?, ?, ?)", ("deafult", "password", "57396917", "low"))
    
    conn.commit()
    conn.close()


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Introduction")
def Introduction():
    return render_template("introduction.html")

@app.route("/Attacks")
def Attacks():
    return render_template("attacks.html")

@app.route("/Resources")
def Resources():
    return render_template("resources.html")

@app.route("/Community")
def Community():
    return render_template("community.html")

@app.route("/private/login")
def start_login():
    return render_template("login.html")

@app.route("/robots.txt")
def robots():
    return render_template("robots.txt")


@app.route("/login/result", methods=["POST"])
def login():
    guess_username = request.form["user_username"]
    guess_password = request.form["user_password"]
    
    conn = sqlite3.connect("./logon.db")
    c = conn.cursor()
    c.execute("SELECT username, password, id, priv FROM pass_table WHERE username='%s' AND password='%s'" % (guess_username, guess_password))

    result = c.fetchall()

    conn.close()
    
    if result:
        return render_template("login_result.html", result=result)
    else:
        return render_template("login_result.html")


if __name__ == "__main__":
    app.run(port=80)
