from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "🚀 API Running"}

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

if __name__ == "__main__":
    app.run(debug=True)