import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """
    Faz a requisição HTTP para o site e retorna o HTML da página.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se ocorreu algum erro na requisição
        return response.text
    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {err}")
        return None
    except Exception as err:
        print(f"Erro ao acessar a URL: {err}")
        return None

def parse_html(html_content):
    """
    Processa o HTML e extrai as informações desejadas.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Exemplo: Extraindo todos os títulos de artigos (elementos <h2>)
    titulos = soup.find_all('h2')
    
    # Extraindo e limpando os títulos (get_text() remove as tags HTML)
    return [titulo.get_text().strip() for titulo in titulos]

def save_results(data, filename="resultados.txt"):
    """
    Salva os resultados extraídos em um arquivo de texto.
    """
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def main():
    # URL do site que desejamos raspar
    url = ''
    
    # Passo 1: Obter o HTML da página
    html_content = fetch_html(url)
    
    # Passo 2: Se o HTML for obtido com sucesso, processá-lo
    if html_content:
        titulos = parse_html(html_content)
        
        # Passo 3: Exibir ou salvar os resultados
        if titulos:
            print("Títulos encontrados:")
            for titulo in titulos:
                print(f"- {titulo}")
            
            # Salvando os títulos em um arquivo
            save_results(titulos, filename="titulos_artigos.txt")
        else:
            print("Nenhum título foi encontrado.")
    else:
        print("Falha ao obter o conteúdo da página.")

if __name__ == "__main__":
    main()
