import asyncio
import urllib.parse
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

async def test_tikwm():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await Stealth().apply_stealth_async(page)
        
        q = urllib.parse.quote('skin tag remover')
        url = f"https://tikwm.com/api/feed/search?keywords={q}&count=5"
        
        print("Navigating...")
        await page.goto(url)
        await page.wait_for_timeout(4000)
        
        html = await page.content()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.text
        
        print(text[:300])
        await browser.close()

asyncio.run(test_tikwm())
