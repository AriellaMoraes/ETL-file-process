import requests


def consume_api(url):
    """
    Função para consumir uma API e retornar o conteúdo.

    Argumentos:
    url (str): A URL da API a ser consumida.

    Retorna:
    dict: O conteúdo da API em formato JSON.
    """
    try:
        # Fazendo a requisição GET para a URL da API
        response = requests.get(url)

        # Verificando se a requisição foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Retornando o conteúdo da resposta (assumindo que a resposta é em formato JSON)
            return response.json()
        else:
            print(f"Erro ao consumir a API: {response.status_code}")
            return None
    except Exception as e:
        print(f"Erro ao consumir a API: {str(e)}")
        return None






