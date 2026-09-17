import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TransparenciaScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.data = []

    # Scraping do Portal da Transparência Federal
    def scrape_federal(self):
        try:
            url = "http://www.portaldatransparencia.gov.br/servidores"  # URL base
            # Exemplo de parâmetros - pode variar conforme a API ou página específica
            params = {
                'pagina': 1,
                'tamanhoPagina': 100
            }
            
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Exemplo de extração - os seletores CSS reais dependerão da estrutura do site
            tabela = soup.select('table.dataTable')
            if tabela:
                for row in tabela[0].find_all('tr')[1:]:  # Pula o cabeçalho
                    cols = row.find_all('td')
                    if len(cols) >= 5:
                        funcionario = {
                            'nivel': 'Federal',
                            'nome': cols[0].text.strip(),
                            'cargo': cols[1].text.strip(),
                            'orgao': cols[2].text.strip(),
                            'salario': cols[3].text.strip(),
                            'regiao': cols[4].text.strip()
                        }
                        self.data.append(funcionario)
            logging.info("Scraping federal concluído")
            
        except Exception as e:
            logging.error(f"Erro no scraping federal: {str(e)}")

    # Scraping Estadual (Exemplo: São Paulo)
    def scrape_estadual_sp(self):
        try:
            url = "http://www.transparencia.sp.gov.br"  # URL base
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Exemplo hipotético - ajustar conforme estrutura real
            funcionarios = soup.select('.funcionario-item')
            for func in funcionarios:
                funcionario = {
                    'nivel': 'Estadual',
                    'nome': func.select_one('.nome').text.strip(),
                    'cargo': func.select_one('.cargo').text.strip(),
                    'orgao': func.select_one('.orgao').text.strip(),
                    'salario': func.select_one('.salario').text.strip(),
                    'regiao': 'São Paulo'
                }
                self.data.append(funcionario)
            logging.info("Scraping estadual (SP) concluído")
            
        except Exception as e:
            logging.error(f"Erro no scraping estadual: {str(e)}")

    # Scraping Municipal (Exemplo: São Paulo)
    def scrape_municipal_sp(self):
        try:
            url = "https://www.prefeitura.sp.gov.br/cidade/secretarias/transparencia"  # URL base
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Exemplo hipotético - ajustar conforme estrutura real
            tabela = soup.select('table.servidores')
            if tabela:
                for row in tabela[0].find_all('tr')[1:]:
                    cols = row.find_all('td')
                    if len(cols) >= 4:
                        funcionario = {
                            'nivel': 'Municipal',
                            'nome': cols[0].text.strip(),
                            'cargo': cols[1].text.strip(),
                            'orgao': cols[2].text.strip(),
                            'salario': cols[3].text.strip(),
                            'regiao': 'São Paulo - SP'
                        }
                        self.data.append(funcionario)
            logging.info("Scraping municipal (SP) concluído")
            
        except Exception as e:
            logging.error(f"Erro no scraping municipal: {str(e)}")

    # Salvar dados em CSV
    def save_to_csv(self, filename='dados_transparencia.csv'):
        try:
            df = pd.DataFrame(self.data)
            df.to_csv(filename, index=False, encoding='utf-8')
            logging.info(f"Dados salvos em {filename}")
        except Exception as e:
            logging.error(f"Erro ao salvar CSV: {str(e)}")

    # Executar todos os scrapings
    def run(self):
        logging.info("Iniciando scraping...")
        self.scrape_federal()
        sleep(2)  # Pausa para evitar bloqueio
        self.scrape_estadual_sp()
        sleep(2)
        self.scrape_municipal_sp()
        self.save_to_csv()

if __name__ == "__main__":
    scraper = TransparenciaScraper()
    scraper.run()
