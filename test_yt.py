import asyncio
import urllib.parse
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def test_yt():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        keyword = "skin tag remover"
        q = urllib.parse.quote(f"{keyword} shorts")
        # sp=EgIYAQ%3D%3D is the filter for < 4 minutes (Shorts/Videos)
        url = f"https://www.youtube.com/results?search_query={q}&sp=EgIYAQ%253D%253D"
        
        print("Navigating to YT...")
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)
        
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        
        links = []
        for a in soup.find_all('a', id='video-title'):
            href = a.get('href')
            title = a.get('title', a.text.strip())
            if href and '/shorts/' in href:
                links.append((title, href))
                
        print(f"Found {len(links)} shorts:")
        for l in links[:5]:
            print(l)
            
        await browser.close()

asyncio.run(test_yt())
