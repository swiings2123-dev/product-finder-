import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import urllib.parse

async def test_ddg_playwright():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        q = urllib.parse.quote('site:tiktok.com/video/ "skin tag remover"')
        url = f"https://html.duckduckgo.com/html/?q={q}"
        
        print("Navigating to DDG...")
        await page.goto(url)
        await page.wait_for_timeout(3000)
        
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        
        links = []
        for a in soup.find_all('a', class_='result__snippet'):
            href = a.get('href', '')
            if 'tiktok.com' in href:
                links.append(href)
                
        print(f"Found {len(links)} links:")
        for l in set(links):
            print(l)
            
        await browser.close()

asyncio.run(test_ddg_playwright())
