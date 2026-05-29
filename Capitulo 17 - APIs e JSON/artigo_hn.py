try:
	import requests
except ImportError:
	raise ImportError("Módulo 'requests' não encontrado. Instale com: pip install requests") from None
import json


# Faça uma chamada de API e armazene a resposta.
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Código de status: {r.status_code}")

# Explore a estrutura dos dados.
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)