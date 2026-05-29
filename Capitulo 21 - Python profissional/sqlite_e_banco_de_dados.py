"""Exemplo de uso de banco de dados SQLite em Python.
"""

import sqlite3
from pathlib import Path

banco = Path('profissional.db')

with sqlite3.connect(banco) as conexao:
    cursor = conexao.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        '''
    )

    cursor.execute('DELETE FROM usuarios')
    conexao.commit()

    usuarios = [
        ('Ana', 'ana@example.com'),
        ('Bruno', 'bruno@example.com'),
        ('Carla', 'carla@example.com'),
    ]

    cursor.executemany('INSERT INTO usuarios (nome, email) VALUES (?, ?)', usuarios)
    conexao.commit()

    cursor.execute('SELECT id, nome, email FROM usuarios')
    for registro in cursor.fetchall():
        print('Usuário:', registro)

print('Banco de dados criado em:', banco)
