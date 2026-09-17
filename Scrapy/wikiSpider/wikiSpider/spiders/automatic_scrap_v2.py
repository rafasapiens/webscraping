import os
import subprocess
from pathlib import Path

# 1. Configuração de caminhos absolutos
HOME = Path.home()
SPIDER_DIR = HOME / "Python_estudos/webscraping/Scrapy/wikiSpider/wikiSpider/spiders"
SCRAPY_BIN = HOME / "Python_estudos/webscraping/Scrapy/scrapy/bin/scrapy"

# Entra na pasta correta das spiders (Equivalente ao 'cd')
os.chdir(SPIDER_DIR)

# 2. Executa o Scrapy usando o binário do venv e o timeout de 5 segundos
print("---> Executando o Scrapy por exatamente 5 segundos...")
subprocess.run(
    f"timeout 5s {SCRAPY_BIN} runspider articleItems.py -o articles.xml:xml",
    shell=True
)

# 3. Adiciona e commita no Git
print("\n---> Salvando no Git local...")
os.system("git add articles.xml")
os.system('git commit -m "xml"')

# 4. Definição das Credenciais e Repositórios
GITLAB_TOKEN = "glpat-3mgTb8ILCcLEgfjXX1m4FWM6MQpvOjEKdTo2NWJ3bw8.01.171t18b14"
GITHUB_TOKEN = "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"

USER_GITLAB = "rafasapiens"
USER_GITHUB = "rafasapiens"

URL_GITLAB = f"https://{USER_GITLAB}:{GITLAB_TOKEN}@gitlab.com/rafasapiens/webscraping.git"
URL_GITHUB = f"https://{USER_GITHUB}:{GITHUB_TOKEN}@github.com/rafasapiens/webscraping.git"

# 5. Envia alterações automaticamente para GitLab e GitHub
print("\n---> Enviando para o GitLab automaticamente...")
os.system(f"git push {URL_GITLAB} HEAD:main")

print("\n---> Enviando para o GitHub (webscraping) automaticamente...")
os.system(f"git push {URL_GITHUB} HEAD:main")

print("\n✅ Processo 100% automático concluído com sucesso!")

