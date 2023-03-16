import requests
import sys

def load_wordlist(wordlist_path):
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        paths = [line.strip() for line in file]
    return paths

def scan_url(url, paths):
    if not url.startswith("http"):
        url = "http://" + url

    if not url.endswith("/"):
        url += "/"

    for path in paths:
        target_url = url + path
        try:
            response = requests.get(target_url)
            if response.status_code == 200:
                print(f"Encontrado: {target_url}")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {target_url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python web_scanner_wordlist.py <url> <wordlist_path>")
        sys.exit(1)

    url = sys.argv[1]
    wordlist_path = sys.argv[2]

    paths = load_wordlist(wordlist_path)
    scan_url(url, paths)
