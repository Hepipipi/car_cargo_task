import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect("db.sqlite3")
with open("dump.sql", "w", encoding="utf-8") as f:
    for line in conn.iterdump():
        f.write(f"{line}\n")
conn.close()
