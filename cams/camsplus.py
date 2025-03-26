import requests
from bs4 import BeautifulSoup
import time

# Configuração do header
headers = {"User-Agent": "Mozilla/5.0"}

# Lista de sites a serem analisados
SITES = {
    "EarthCam": "https://www.earthcam.com/network/",
    "WebcamTaxi": "https://www.webcamtaxi.com/en/",
    "SkylineWebcams": "https://www.skylinewebcams.com/",
    "Windy": "https://www.windy.com/webcams",
    "CamStreamer": "https://camstreamer.com/live",
    # LiveCams Pro não tem um site fixo claro, geralmente é um app; vamos usar um exemplo genérico
    "LiveCamsPro": "https://www.earthcam.com/"  # Substituí por EarthCam como placeholder
}

def fetch_page(url):
    """Faz a requisição HTTP e retorna o soup"""
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
        return None

def parse_earthcam(soup):
    """Parser para EarthCam"""
    cameras = []
    for item in soup.select('div.webcam-item'):  # Ajuste o seletor conforme o HTML real
        link = item.find('a')
        if link and link.get('href'):
            cam_url = link.get('href') if link.get('href').startswith('http') else f"https://www.earthcam.com{link.get('href')}"
            title = link.get('title', link.text.strip())
            cameras.append({"title": title, "url": cam_url, "source": "EarthCam"})
    return cameras

def parse_webcamtaxi(soup):
    """Parser para Webcam Taxi"""
    cameras = []
    for link in soup.select('a[href*="/en/"]'):  # Links de câmeras geralmente têm /en/
        cam_url = link.get('href') if link.get('href').startswith('http') else f"https://www.webcamtaxi.com{link.get('href')}"
        title = link.text.strip() or link.get('title', '')
        if title and 'webcam' in cam_url.lower():
            cameras.append({"title": title, "url": cam_url, "source": "WebcamTaxi"})
    return cameras

def parse_skylinewebcams(soup):
    """Parser para Skyline Webcams"""
    cameras = []
    for link in soup.select('a[href*="/webcam/"]'):
        cam_url = link.get('href') if link.get('href').startswith('http') else f"https://www.skylinewebcams.com{link.get('href')}"
        title = link.text.strip() or link.get('title', '')
        cameras.append({"title": title, "url": cam_url, "source": "SkylineWebcams"})
    return cameras

def parse_windy(soup):
    """Parser para Windy"""
    cameras = []
    for link in soup.select('a[href*="/webcams/"]'):
        cam_url = link.get('href') if link.get('href').startswith('http') else f"https://www.windy.com{link.get('href')}"
        title = link.text.strip() or link.get('title', '')
        cameras.append({"title": title, "url": cam_url, "source": "Windy"})
    return cameras

def parse_camstreamer(soup):
    """Parser para CamStreamer"""
    cameras = []
    for link in soup.select('a[href*="/live"]'):
        cam_url = link.get('href') if link.get('href').startswith('http') else f"https://camstreamer.com{link.get('href')}"
        title = link.text.strip() or link.get('title', '')
        cameras.append({"title": title, "url": cam_url, "source": "CamStreamer"})
    return cameras

def parse_livecamspro(soup):
    """Parser genérico para LiveCams Pro (usando EarthCam como placeholder)"""
    return parse_earthcam(soup)  # Placeholder, substituir por parser real se houver URL específica

PARSERS = {
    "EarthCam": parse_earthcam,
    "WebcamTaxi": parse_webcamtaxi,
    "SkylineWebcams": parse_skylinewebcams,
    "Windy": parse_windy,
    "CamStreamer": parse_camstreamer,
    "LiveCamsPro": parse_livecamspro
}

def get_all_cameras():
    """Busca câmeras em todos os sites"""
    all_cameras = []
    
    for site_name, site_url in SITES.items():
        print(f"\nProcessando {site_name} ({site_url})...")
        soup = fetch_page(site_url)
        if soup:
            cameras = PARSERS[site_name](soup)
            print(f"Encontradas {len(cameras)} câmeras em {site_name}")
            all_cameras.extend(cameras)
        else:
            print(f"Falha ao processar {site_name}")
        time.sleep(2)  # Delay para evitar bloqueios
        
    return all_cameras

def main():
    print("Iniciando busca por câmeras nos sites...")
    cameras = get_all_cameras()
    
    # Exibir resultados
    print("\n=== Lista Completa de Câmeras Encontradas ===")
    for idx, cam in enumerate(cameras, 1):
        print(f"\nCâmera {idx}:")
        print(f"Fonte: {cam['source']}")
        print(f"Título: {cam['title']}")
        print(f"URL: {cam['url']}")
    
    print(f"\nTotal de câmeras encontradas: {len(cameras)}")

if __name__ == "__main__":
    main()
