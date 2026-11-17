import os
import time

import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify

app = Flask(__name__)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "app-db"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "user": os.getenv("DB_USER", "appuser"),
    "password": os.getenv("DB_PASSWORD", "apppass"),
    "dbname": os.getenv("DB_NAME", "appdb"),
}


def get_connection(retries=10, delay=2):
    last_err = None
    for _ in range(retries):
        try:
            return psycopg2.connect(**DB_CONFIG)
        except psycopg2.OperationalError as err:
            last_err = err
            time.sleep(delay)
    raise last_err


@app.route("/")
def index():
    return jsonify(message="app-service is running", try_endpoint="/api/data")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/api/data")
def get_data():
    try:
        conn = get_connection()
        with conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id, name, description, created_at FROM items ORDER BY id;")
            rows = cur.fetchall()
        conn.close()
        for r in rows:
            r["created_at"] = r["created_at"].isoformat()
        return jsonify(status="success", database="connected", count=len(rows), data=rows)
    except Exception as exc:
        return jsonify(status="error", database="unreachable", error=str(exc)), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
