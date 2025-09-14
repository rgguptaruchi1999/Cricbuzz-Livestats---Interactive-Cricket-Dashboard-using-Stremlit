import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "cricbuzz.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("\n📂 Tables in Database:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(tables)

for table in tables:
    tname = table[0]
    print(f"\n🔹 Table: {tname}")
    cursor.execute(f"PRAGMA table_info({tname});")
    for col in cursor.fetchall():
        print(col)

conn.close()

