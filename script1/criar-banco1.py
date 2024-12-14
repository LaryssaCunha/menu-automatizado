import sqlite3

conn = sqlite3.connect("loja.db")
cursor = conn.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS loja (
                ano INTEGER NOT NULL,
                mes INTEGER NOT NULL,
                faturamento REAL NOT NULL,
                despesas REAL NOT NULL
                )
               """)

conn.commit()
cursor.close()
conn.close()