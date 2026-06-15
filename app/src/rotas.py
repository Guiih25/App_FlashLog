import requests

base_url = "http://10.135.232.36:5006"

def rastrear_encomenda(codigo):
    url = f"{base_url}/pesquisar_encomenda"

    dados = {
        "termo": codigo,
    }

    result = requests.post(url, json=dados)

    return result.json()