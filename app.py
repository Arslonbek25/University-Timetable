from flask import Flask, render_template, request
import pg8000
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("DB_NAME", "Arslan")
DB_USER = os.environ.get("DB_USER", "student")
DB_PASS = os.environ.get("DB_PASS", "student_pass")


def get_db_connection():
    return pg8000.connect(
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=5432,
        database=DB_NAME,
    )


@app.route("/", methods=["GET"])
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT DISTINCT level FROM Timetable ORDER BY level;"
    cur.execute(query)
    levels = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("index.html", levels=levels)


@app.route("/timetable", methods=["GET"])
def timetable():
    level = request.args.get("level")
    if not level:
        return "Level not specified", 400

    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT course_id, course_name, day, time, room FROM Timetable WHERE level = %s;"
    cur.execute(query, (level,))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    message = "No data found for this level." if not rows else None

    return render_template("timetable.html", data=rows, message=message, level=level)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
