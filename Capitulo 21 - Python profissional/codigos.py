from pathlib import Path
import sqlite3

caminho = Path('dados.db')
conn = sqlite3.connect(caminho)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS pessoas (nome TEXT, idade INTEGER)')
cursor.execute('INSERT INTO pessoas VALUES (?, ?)', ('Ana', 30))
conn.commit()
for row in cursor.execute('SELECT nome, idade FROM pessoas'):
    print(row)
conn.close()
