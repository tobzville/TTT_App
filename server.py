from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'admin'


@app.route("/")
def main():
    return render_template('login_page.html')

@app.route("/TTT")
def route_TTT():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * from TTT")
    data = cursor.fetchone()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)