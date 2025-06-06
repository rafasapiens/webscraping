import requests
from bs4 import BeautifulSoup
import json
import csv

# Configuração do header
headers = {"User-Agent": "Mozilla/5.0"}

def get_city_links():
    """Obtém os links das cidades da página principal"""
    try:
        html = requests.get('http://www.insecam.org/en/mapcity/', headers=headers).content
        soup = BeautifulSoup(html, 'html.parser')
        
        cities_links = []
        for link in soup.find_all('a', href=lambda href: href and '/en/bycity/' in href):
            city_name = link.text.split('/')[0].strip()
            city_url = 'http://www.insecam.org' + link.get('href')
            cities_links.append({"Cidade": city_name, "Link": city_url})
        
        return cities_links
    except Exception as e:
        print(f"Erro ao obter links das cidades: {e}")
        return []

def get_cameras_from_city(city_url):
    """Obtém as câmeras de uma URL de cidade específica"""
    try:
        html = requests.get(city_url, headers=headers).content
        soup = BeautifulSoup(html, 'html.parser')
        cameras = []
        
        for cam in soup.select('div.col-xs-12.col-sm-6.col-md-4.col-lg-4'):
            link = cam.find('a')
            if link:
                camera_data = {
                    'title': link.get('title', '').strip(),
                    'url': 'http://www.insecam.org' + link.get('href', '').strip(),
                    'image': link.find('img').get('src', '').strip() if link.find('img') else '',
                    'location': link.get_text(strip=True).split('\n')[-1]
                }
                cameras.append(camera_data)
        
        return cameras
    except Exception as e:
        print(f"Erro ao obter câmeras de {city_url}: {e}")
        return []

def save_to_json(data, filename="cameras.json"):
    """Salva os dados em um arquivo JSON"""
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"Dados salvos em {filename}")
    except Exception as e:
        print(f"Erro ao salvar JSON: {e}")

def save_to_csv(data, filename="cameras.csv"):
    """Salva os dados em um arquivo CSV"""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['city', 'title', 'url', 'image', 'location']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()
            for cam in data:
                writer.writerow(cam)
        print(f"Dados salvos em {filename}")
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")

def main():
    print("Obtendo lista de cidades...")
    cities = get_city_links()
    
    if not cities:
        print("Nenhuma cidade encontrada.")
        return
    
    all_cameras = []
    
    # Para cada cidade, obter as câmeras
    for idx, city in enumerate(cities, 1):
        print(f"\nProcessando cidade {idx}/{len(cities)}: {city['Cidade']}")
        cameras = get_cameras_from_city(city['Link'])
        
        for cam in cameras:
            cam['city'] = city['Cidade']  # Adiciona o nome da cidade à câmera
            all_cameras.append(cam)
        
        print(f"Encontradas {len(cameras)} câmeras em {city['Cidade']}")
    
    # Exibir resultados finais
    print("\n=== Lista Completa de Câmeras Encontradas ===")
    for idx, cam in enumerate(all_cameras, 1):
        print(f"\nCâmera {idx}:")
        print(f"Cidade: {cam['city']}")
        print(f"Título: {cam['title']}")
        print(f"URL: {cam['url']}")
        print(f"Imagem: {cam['image']}")
        print(f"Localização: {cam['location']}")
    
    # Salvar em JSON e CSV
    save_to_json(all_cameras)
    save_to_csv(all_cameras)

if __name__ == "__main__":
    main()
