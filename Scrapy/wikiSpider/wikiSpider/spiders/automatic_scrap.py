import os
import sys
import subprocess
from pathlib import Path

# 1. NAVEGAÇÃO DE DIRETÓRIO (Equivalente ao 'cd')
HOME = Path.home()
SPIDER_DIR = HOME / "Python_estudos/webscraping/Scrapy/wikiSpider/wikiSpider/spiders"

# Troca o diretório de trabalho para a pasta das spiders
os.chdir(SPIDER_DIR)
print(f"---> Diretório atual ajustado para: {os.getcwd()}")

# 2. VIRTUALENV (Equivalente ao 'source .../activate')
# Aponta diretamente para o binário do Scrapy dentro do ambiente virtual ativo
VENV_SCRAPY = HOME / "Python_estudos/webscraping/Scrapy/scrapy/bin/scrapy"

# 3. EXECUÇÃO DO SCRAPY (Limitado a 5 segundos)
print("\n---> Executando o Scrapy por 5 segundos...")
subprocess.run(
    f"timeout 5s {VENV_SCRAPY} runspider articleItems.py -o articles.xml:xml",
    shell=True
)

# 4. GIT ADD E COMMIT
print("\n---> Salvando no Git local...")
os.system("git add articles.xml")
os.system('git commit -m "xml"')

# 5. CREDENCIAIS E PUSH AUTOMÁTICO
GITLAB_TOKEN = "glpat-3mgTb8ILCcLEgfjXX1m4FWM6MQpvOjEKdTo2NWJ3bw8.01.171t18b14"
GITHUB_TOKEN = "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"

USER_GITLAB = "rafasapiens"
USER_GITHUB = "rafasapiens"

URL_GITLAB = f"https://{USER_GITLAB}:{GITLAB_TOKEN}@gitlab.com/rafasapiens/webscraping.git"
URL_GITHUB = f"https://{USER_GITHUB}:{GITHUB_TOKEN}@github.com/rafasapiens/webscraping.git"

print("\n---> Enviando para o GitLab automaticamente...")
os.system(f"git push {URL_GITLAB} HEAD:main")

print("\n---> Enviando para o GitHub (webscraping) automaticamente...")
os.system(f"git push {URL_GITHUB} HEAD:main")

print("\n✅ Processo 100% automático concluído com sucesso!")



'''


import os
import subprocess

# 1. Executa o Scrapy por exatamente 5 segundos
print("---> Executando o Scrapy por exatamente 5 segundos...")
subprocess.run(
    "timeout 5s scrapy runspider articleItems.py -o articles.xml:xml",
    shell=True
)

# 2. Adiciona e commita no Git
print("\n---> Salvando no Git local...")
os.system("git add articles.xml")
os.system('git commit -m "xml"')

# 3. Definição das Credenciais
GITLAB_TOKEN = "glpat-3mgTb8ILCcLEgfjXX1m4FWM6MQpvOjEKdTo2NWJ3bw8.01.171t18b14"
GITHUB_TOKEN = "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"

USER_GITLAB = "rafasapiens"
USER_GITHUB = "rafasapiens"

# URLs com autenticação embutida (injetando o token como senha)
URL_GITLAB = f"https://{USER_GITLAB}:{GITLAB_TOKEN}@gitlab.com/rafasapiens/webscraping.git"
URL_GITHUB = f"https://{USER_GITHUB}:{GITHUB_TOKEN}@github.com/rafasapiens/webscraping.git"

# 4. Envia alterações automaticamente para GitLab e GitHub
print("\n---> Enviando para o GitLab automaticamente...")
os.system(f"git push {URL_GITLAB} HEAD:main")

print("\n---> Enviando para o GitHub (webscraping) automaticamente...")
os.system(f"git push {URL_GITHUB} HEAD:main")

print("\n✅ Processo 100% automático concluído com sucesso!")


'''
