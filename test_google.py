import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

def test():
    keyword = "skin tag remover"
    q = f"site:tiktok.com/video/ {keyword}"
    url = f"https://www.google.com/search?q={urllib.parse.quote(q)}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    r = requests.get(url, headers=headers)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if 'tiktok.com' in href and '/video/' in href:
            # clean google redirect urls if any
            match = re.search(r'(https://www\.tiktok\.com/.*?/video/\d+)', href)
            if match:
                links.append(match.group(1))
    
    print(list(set(links)))

test()
