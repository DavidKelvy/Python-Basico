from pathlib import Path
import json


def get_stored_username(path):
    """Obtenha o nome de usuário armazenado, se disponível."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def greet_user():
    """Cumprimente o usuário pelo nome."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("Qual o seu nome? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()