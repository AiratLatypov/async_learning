from flask import Flask, jsonify
import psycopg2

from chapter_05.database import DB_NAME, DB_USER, DB_PASS, DB_HOST

app = Flask(__name__)


conn_info = f"dbname={DB_NAME} user={DB_USER} password={DB_PASS} host={DB_HOST}"
db = psycopg2.connect(conn_info)


@app.route("/brands")
def brands():
    cur = db.cursor()
    cur.execute("SELECT brand_id, brand_name FROM brand")
    rows = cur.fetchall()
    cur.close()
    return jsonify([{"brand_id": row[0], "brand_name": row[1]} for row in rows])
