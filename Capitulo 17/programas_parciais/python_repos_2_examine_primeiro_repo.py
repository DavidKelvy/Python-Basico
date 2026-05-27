import requests


# Faça uma chamada de API e verifique a resposta.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Código de status: {r.status_code}")

# Converta o objeto de resposta em um dicionário.
response_dict = r.json()

print(f"Repositórios totais: {response_dict['total_count']}")
print(f"Resultados completos: {not response_dict['incomplete_results']}")

# Explore informações sobre os repositórios.
repo_dicts = response_dict['items']
print(f"Repositórios retornados: {len(repo_dicts)}")

# Examine o primeiro repositório.
repo_dict = repo_dicts[0]

print("\nSelected information about first repository:")
print(f"Nome: {repo_dict['name']}")
print(f"Proprietário: {repo_dict['owner']['login']}")
print(f"Estrelas: {repo_dict['stargazers_count']}")
print(f"Repositório: {repo_dict['html_url']}")
print(f"Criado: {repo_dict['created_at']}")
print(f"Atualizado: {repo_dict['updated_at']}")
print(f"Descrição: {repo_dict['description']}")