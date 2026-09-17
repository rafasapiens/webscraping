import requests
from bs4 import BeautifulSoup

def buscar_livros(termo):
    # A URL de busca da Estante Virtual
    url = f"https://www.estantevirtual.com.br/busca?q={termo.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar os elementos que contêm os livros
    # Nota: Você precisará inspecionar o HTML atual da Estante para pegar a classe correta
    livros = soup.find_all('div', class_='nome-da-classe-do-produto')
    
    for livro in livros:
        print(f"Encontrado: {livro.text.strip()}")

# Execução
buscar_livros("Trevo Negro Cedibra")



print("Fim do primeiro programa!")

print("Inicio do segyndo programa!")




import requests
from bs4 import BeautifulSoup
import time

def monitorar_estante(termo):
    # Simula um navegador para evitar bloqueios de bot
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    url = f"https://www.estantevirtual.com.br/busca?q={termo.replace(' ', '+')}"

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # O seletor abaixo deve ser ajustado conforme a estrutura atual da página
            livros = soup.find_all('div', class_='book-item') # Ajuste conforme inspeção

            print(f"--- Resultados encontrados para: {termo} ---")
            for livro in livros[:5]: # Traz os 5 primeiros
                titulo = livro.find('h2').text.strip()
                preco = livro.find('span', class_='price').text.strip()
                print(f"Título: {titulo} | Preço: {preco}")
        else:
            print(f"Erro ao acessar o site: {response.status_code}")
    except Exception as e:
        print(f"Erro de conexão: {e}")

# Rodar a busca
monitorar_estante("Trevo Negro Cedibra")

