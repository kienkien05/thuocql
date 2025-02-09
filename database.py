import sqlite3

conn = sqlite3.connect("pharmacy.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER DEFAULT 0,
        price REAL DEFAULT 0,
        import_date TEXT DEFAULT CURRENT_DATE
    )
""")

conn.commit()
conn.close()

print("Đã tạo database!")
