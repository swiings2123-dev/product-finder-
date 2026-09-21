import asyncio
import urllib.parse
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

async def test_google_pw2():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        q = urllib.parse.quote('site:urlebird.com/video/ "skin tag remover"')
        url = f"https://www.google.com/search?q={q}"
        
        print("Navigating to Google...")
        await page.goto(url)
        await page.wait_for_timeout(3000)
        
        # Check for consent button and click if exists
        try:
            await page.locator("text='Accept all'").click(timeout=2000)
            await page.wait_for_timeout(2000)
        except:
            pass
            
        html = await page.content()
        with open('google_out.html', 'w', encoding='utf-8') as f:
            f.write(html)
            
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

asyncio.run(test_google_pw2())
