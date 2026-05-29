# Comece com os usuários que precisam ser verificados,
# e uma lista vazia para conter usuários confirmados.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verifique cada usuário até não haver mais usuários não confirmados.
# Mova cada usuário verificado para a lista de usuários confirmados.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verificando usuário: {current_user.title()}")
    confirmed_users.append(current_user)
    
# Exiba todos os usuários confirmados.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())