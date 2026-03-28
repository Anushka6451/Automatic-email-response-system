from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message": "🚀 Email Auto Response API is running",
        "endpoint": "/stats"
    }


@app.route("/stats")
def stats():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM emails")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT category, COUNT(*) FROM emails GROUP BY category")
    categories = dict(cursor.fetchall())

    conn.close()

    return jsonify({
        "total": total,
        "categories": categories
    })