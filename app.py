from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("pharmacy.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    medicines = conn.execute("SELECT * FROM medicines").fetchall()
    conn.close()
    return render_template("index.html", medicines=medicines)

@app.route("/save_medicines", methods=["POST"])
def save_medicines():
    data = request.json  
    if not data or not isinstance(data, list):
        return jsonify({"message": "Dữ liệu không hợp lệ!"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    for med in data:
        cursor.execute("UPDATE medicines SET name = ?, quantity = ?, price = ? WHERE id = ?", 
                       (med["name"], med["quantity"], med["price"], med["id"]))

    conn.commit()
    conn.close()

    return jsonify({"message": "Lưu thành công!"}), 200

@app.route("/add_medicine", methods=["POST"])
def add_medicine():
    data = request.json  
    if not data or "name" not in data or "quantity" not in data or "price" not in data:
        return jsonify({"message": "Thiếu thông tin!"}), 400

    conn = get_db_connection()
    conn.execute("INSERT INTO medicines (name, quantity, price, import_date) VALUES (?, ?, ?, date('now'))", 
                 (data["name"], data["quantity"], data["price"]))
    conn.commit()
    conn.close()

    return jsonify({"message": "Thêm thuốc thành công!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
