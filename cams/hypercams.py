import requests
from bs4 import BeautifulSoup
import json
import csv
import shodan
import time
from urllib.parse import urljoin

# Configuração do header
headers = {"User-Agent": "Mozilla/5.0"}

# Substitua pelas suas chaves de API
SHODAN_API_KEY = "SUA_CHAVE_SHODAN_AQUI"  # Obtenha em shodan.io
ZOOMEYE_API_KEY = "SUA_CHAVE_ZOOMEYE_AQUI"  # Obtenha em zoomeye.org (se disponível)

# Portas comuns para câmeras IP
COMMON_PORTS = [80, 554, 8080, 81]
# Endpoints comuns de streaming
COMMON_ENDPOINTS = ["/video", "/stream", "/mjpg/video.mjpg", "/live", "/snapshot"]

def get_city_links():
    """Obtém os links das cidades da página principal do Insecam"""
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
    """Obtém as câmeras de uma URL de cidade específica (Insecam)"""
    try:
        html = requests.get(city_url, headers=headers, timeout=5).content
        soup = BeautifulSoup(html, 'html.parser')
        cameras = []
        for cam in soup.select('div.col-xs-12.col-sm-6.col-md-4.col-lg-4'):
            link = cam.find('a')
            if link:
                camera_data = {
                    'title': link.get('title', '').strip(),
                    'url': 'http://www.insecam.org' + link.get('href', '').strip(),
                    'image': link.find('img').get('src', '').strip() if link.find('img') else '',
                    'location': link.get_text(strip=True).split('\n')[-1],
                    'source': 'Insecam'
                }
                cameras.append(camera_data)
        return cameras
    except Exception as e:
        print(f"Erro ao obter câmeras de {city_url}: {e}")
        return []

def get_shodan_cameras():
    """Busca câmeras IP usando a API do Shodan"""
    cameras = []
    if not SHODAN_API_KEY:
        print("Chave Shodan não fornecida. Pulando busca no Shodan.")
        return cameras
    
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        # Consulta comum para câmeras: "webcam", "camera", portas RTSP ou HTTP
        results = api.search("webcam port:80,554 os:Linux has_screenshot:true")
        for result in results['matches']:
            ip = result['ip_str']
            port = result['port']
            url = f"http://{ip}:{port}"
            camera_data = {
                'title': result.get('title', 'Unknown Camera'),
                'url': url,
                'image': result.get('screenshot', {}).get('data', '') if 'screenshot' in result else '',
                'location': result.get('location', {}).get('country_name', 'Unknown'),
                'source': 'Shodan'
            }
            cameras.append(camera_data)
        print(f"Encontradas {len(cameras)} câmeras via Shodan")
    except shodan.APIError as e:
        print(f"Erro na API Shodan: {e}")
    return cameras

def test_ip_camera(ip, ports=COMMON_PORTS, endpoints=COMMON_ENDPOINTS):
    """Testa portas e endpoints comuns em um IP para encontrar streams de câmera"""
    cameras = []
    for port in ports:
        base_url = f"http://{ip}:{port}"
        for endpoint in endpoints:
            test_url = urljoin(base_url, endpoint)
            try:
                response = requests.get(test_url, headers=headers, timeout=3)
                if response.status_code == 200 and ('image' in response.headers.get('Content-Type', '').lower() or 'video' in response.headers.get('Content-Type', '').lower()):
                    cameras.append({
                        'title': f"Camera at {ip}:{port}",
                        'url': test_url,
                        'image': test_url if 'image' in response.headers.get('Content-Type', '').lower() else '',
                        'location': 'Unknown (Direct IP)',
                        'source': 'IP Scan'
                    })
            except requests.RequestException:
                continue
    return cameras

def get_ip_cameras_from_shodan():
    """Usa Shodan para encontrar IPs e testa portas/endpoints"""
    cameras = []
    if not SHODAN_API_KEY:
        print("Chave Shodan não fornecida. Pulando varredura de IPs.")
        return cameras
    
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        results = api.search("port:80,554 os:Linux webcam")
        for result in results['matches']:
            ip = result['ip_str']
            cams = test_ip_camera(ip)
            cameras.extend(cams)
    except shodan.APIError as e:
        print(f"Erro na API Shodan para IPs: {e}")
    return cameras

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
            fieldnames = ['title', 'url', 'image', 'location', 'source', 'city']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for cam in data:
                writer.writerow({k: cam.get(k, '') for k in fieldnames})  # Preenche campos ausentes com ''
        print(f"Dados salvos em {filename}")
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")

def main():
    all_cameras = []

    # 1. Insecam (cidades)
    print("Obtendo lista de cidades do Insecam...")
    cities = get_city_links()
    if cities:
        for idx, city in enumerate(cities, 1):
            print(f"\nProcessando cidade {idx}/{len(cities)}: {city['Cidade']}")
            cameras = get_cameras_from_city(city['Link'])
            for cam in cameras:
                cam['city'] = city['Cidade']
                all_cameras.append(cam)
            print(f"Encontradas {len(cameras)} câmeras em {city['Cidade']}")
    else:
        print("Nenhuma cidade encontrada no Insecam.")

    # 2. Shodan (câmeras diretas)
    print("\nBuscando câmeras via Shodan...")
    shodan_cameras = get_shodan_cameras()
    all_cameras.extend(shodan_cameras)

    # 3. IPs diretos com teste de portas/endpoints
    print("\nTestando IPs do Shodan para streams diretos...")
    ip_cameras = get_ip_cameras_from_shodan()
    all_cameras.extend(ip_cameras)

    # Exibir resultados
    print("\n=== Lista Completa de Câmeras Encontradas ===")
    for idx, cam in enumerate(all_cameras, 1):
        print(f"\nCâmera {idx}:")
        print(f"Fonte: {cam['source']}")
        print(f"Título: {cam['title']}")
        print(f"URL: {cam['url']}")
        print(f"Imagem: {cam['image']}")
        print(f"Localização: {cam['location']}")
        if 'city' in cam:
            print(f"Cidade: {cam['city']}")

    # Salvar em JSON e CSV
    save_to_json(all_cameras)
    save_to_csv(all_cameras)
    print(f"\nTotal de câmeras encontradas: {len(all_cameras)}")

if __name__ == "__main__":
    main()
