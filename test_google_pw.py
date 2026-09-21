import asyncio
import urllib.parse
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

async def test_google_playwright():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        keyword = "skin tag remover"
        q = f"site:urlebird.com/video/ {keyword}"
        url = f"https://www.google.com/search?q={urllib.parse.quote(q)}"
        
        print("Navigating to Google...")
        await page.goto(url)
        await page.wait_for_timeout(3000)
        
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            if 'urlebird.com/video/' in href:
                links.append(href)
                
        print(f"Found {len(links)} links:")
        for l in set(links):
            print(l)
            
        await browser.close()

asyncio.run(test_google_playwright())
