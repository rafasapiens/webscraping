for start scrapy type: scrapy runspider name.py
para rodar o scrapy digite: scrapy runspider nomedoarquivo.py

Scrapy usa os objetos Item para determinar quais informações das
páginas visitadas devem ser salvas. Essas informações podem ser salvas
pelo Scrapy em diversos formatos, por exemplo, arquivos CSV, JSON ou
XML, usando os comandos a seguir:
$ scrapy runspider articleItems.py -o articles.csv -t csv
$ scrapy runspider articleItems.py -o articles.json -t json
$ scrapy runspider articleItems.py -o articles.xml -t xml
Cada um desses comandos executa o scraper articleItems e escreve a saída
no formato e no arquivo especificados. O arquivo será criado caso ainda
não exista.
