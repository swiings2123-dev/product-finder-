import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from bs4 import BeautifulSoup

async def test_ub_visible():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=["--no-sandbox"])
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 720}
        )
        page = await context.new_page()
        await Stealth().apply_stealth_async(page)
        
        print("Navigating...")
        await page.goto("https://urlebird.com/search/?q=skin+tag+remover", wait_until="domcontentloaded", timeout=60000)
        
        # Wait a bit for cloudflare to solve if needed
        await page.wait_for_timeout(5000)
        title = await page.title()
        print(f"Title: {title}")
        
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        cards = soup.find_all('div', class_='thumb')
        print(f"Found {len(cards)} cards")
        
        await browser.close()

asyncio.run(test_ub_visible())
