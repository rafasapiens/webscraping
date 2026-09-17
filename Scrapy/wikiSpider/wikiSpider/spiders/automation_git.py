import os
import subprocess

'''
# 1. Executa o scraper limitando a 5 segundos via argumento do Scrapy
print("---> Executando o Scrapy por 5 segundos...")
subprocess.run([
    "scrapy", "runspider", "articleItems.py",
    "-o", "articles.xml:xml",
    "-s", "CLOSESPIDER_TIMEOUT=5"
])
'''

print("---> Executando o Scrapy por exatamente 5 segundos...")
# O utilitário 'timeout 5s' força o encerramento do processo em 5 segundos
# independente de requisições pendentes no Scrapy.
subprocess.run(
    "timeout 5s scrapy runspider articleItems.py -o articles.xml:xml",
    shell=True
)

# 2. Adiciona e commita no Git
print("\n---> Salvando no Git local...")
os.system("git add articles.xml")
os.system('git commit -m "xml"')

# 3. Exibe os tokens na tela para você copiar/colar durante a pausa do terminal
GITLAB_TOKEN = "glpat-3mgTb8ILCcLEgfjXX1m4FWM6MQpvOjEKdTo2NWJ3bw8.01.171t18b14"
GITHUB_TOKEN = "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"

print("\n================ CREDENCIAIS PARA COPIAR ================")
print(f"Token GitLab: {GITLAB_TOKEN}")
print(f"Token GitHub: {GITHUB_TOKEN}")
print("=========================================================\n")

# 4. Envia para o GitLab e GitHub (o terminal vai pausar pedindo Usuário/Senha)
print("---> Fazendo push para o GitLab (insira as credenciais se solicitado)...")
os.system("git push gitlab")

print("\n---> Fazendo push para o repositório webscraping (insira as credenciais se solicitado)...")
os.system("git push webscraping")

print("\n✅ Processo concluído com sucesso!")



'''

import os
import subprocess

# 1. Executa o scraper limitando a 5 segundos via argumento do Scrapy
print("---> Executando o Scrapy por 5 segundos...")
subprocess.run([
    "scrapy", "runspider", "articleItems.py",
    "-o", "articles.xml:xml",
    "-s", "CLOSESPIDER_TIMEOUT=5"
])

print("---> Executando o Scrapy por exatamente 5 segundos...")

# O utilitário 'timeout 5s' força o encerramento do processo em 5 segundos
# independente de requisições pendentes no Scrapy.
subprocess.run(
    "timeout 5s scrapy runspider articleItems.py -o articles.xml:xml",
    shell=True
)


# 2. Adiciona e commita no Git
print("\n---> Salvando no Git local...")
os.system("git add articles.xml")
os.system('git commit -m "xml"')

# 3. Definição dos tokens extraídos da sua lista
GITLAB_TOKEN = "glpat-3mgTb8ILCcLEgfjXX1m4FWM6MQpvOjEKdTo2NWJ3bw8.01.171t18b14"
GITHUB_TOKEN = "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"

# Usuário Git
USER_GITLAB = "glpat-3mgTb8ILCcLEgfjXX1m4FWM6MQpvOjEKdTo2NWJ3bw8.01.171t18b14"

USER_GITHUB = "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"
# Altere se o usuário do GitHub for diferente

# URL dos repositórios remotos
# IMPORTANTE: Altere "nome-do-repositorio" pelo nome exato do seu projeto no GitLab/GitHub
URL_GITLAB = f"https://{USER_GITLAB}:{GITLAB_TOKEN}@gitlab.com/{USER_GITLAB}/nome-do-repositorio.git"
URL_GITHUB = f"https://{USER_GITHUB}:{GITHUB_TOKEN}@github.com/{USER_GITHUB}/nome-do-repositorio.git"

# 4. Envia para o GitLab e GitHub automaticamente usando os Tokens
print("\n---> Fazendo push automático para o GitLab...")
os.system(f"git push gitlab {USER_GITLAB} ")  # Altere 'main' para 'master' se sua branch principal for master

print("\n---> Fazendo push automático para o repositório webscraping...")
os.system(f"git push webscraping {USER_GITHUB}")  # Altere 'main' para 'master' se necessário

print("\n✅ Processo concluído com sucesso!")

'''

'''

import os
import subprocess

print("---> Executando o Scrapy por exatamente 5 segundos...")

# O utilitário 'timeout 5s' força o encerramento do processo em 5 segundos
# independente de requisições pendentes no Scrapy.
subprocess.run(
    "timeout 5s scrapy runspider articleItems.py -o articles.xml:xml",
    shell=True
)

# 2. Adiciona e commita no Git
print("\n---> Salvando no Git local...")
os.system("git add articles.xml")
os.system('git commit -m "xml"')

# 3. Definição dos tokens
GITLAB_TOKEN = "glpat-3mgTb8ILCcLEgfjXX1m4FWM6MQpvOjEKdTo2NWJ3bw8.01.171t18b14"
GITHUB_TOKEN = "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"

USER_GITLAB = "rafasapiens"
USER_GITHUB = "rafasapiens"  # Altere se seu usuário no GitHub for diferente

# IMPORTANTE: Altere "nome-do-repositorio" abaixo para o nome real dos repositórios
URL_GITLAB = f"https://{USER_GITLAB}:{GITLAB_TOKEN}@gitlab.com/{USER_GITLAB}/nome-do-repositorio.git"
URL_GITHUB = f"https://{USER_GITHUB}:{GITHUB_TOKEN}@github.com/{USER_GITHUB}/nome-do-repositorio.git"

# 4. Envia para o GitLab e GitHub automaticamente usando os Tokens
print("\n---> Fazendo push automático para o GitLab...")
os.system(f"git push {URL_GITLAB} HEAD")

print("\n---> Fazendo push automático para o repositório webscraping...")
os.system(f"git push {URL_GITHUB} HEAD")

print("\n✅ Processo e Push concluídos!")

'''

'''import os
import time
import subprocess

#subprocess.run("timeout 5  scrapy runspider articleItems.py -o articles.xml")
subprocess.run(["scrapy", "runspider", "articleItems.py", "-o", "articles.xml"])

#os.system("source ~/Python_estudos/webscraping/Scrapy/scrapy/bin/activate")
#os.system("cd ~/Python_estudos/webscraping/Scrapy/wikiSpider/wikiSpider/spiders")

#print("scrapy runspider articleItems.py -o articles.xml -t xml")
# os.system("timeout 4")
#os.system("timeout 10  scrapy runspider articleItems.py -o articles.xml")
    
#time.sleep(2)
#os.system("ctrl+z")
#break
    
os.system("git status")
os.system("git add articles.xml")
os.system('git commit -m "xml"')

os.system("git status")
print("rafasapiens\n glpat-3mgTb8ILCcLEgfjXX1m4FWM6MQpvOjEKdTo2NWJ3bw8.01.171t18b14

glpat-rmg7ZUG8iz393x9bVbcYIG86MQp1OjY1YndvCw.01.12127nkxf \n

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






")
os.system("git push")

os.system("git push webscraping")
os.system("git status")
'''
