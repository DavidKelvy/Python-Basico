def greet_users(names):
    """Imprima uma saudação simples para cada usuário da lista."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)