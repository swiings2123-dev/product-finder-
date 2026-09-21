import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

async def test_ub():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        await Stealth().apply_stealth_async(page)
        
        await page.goto("https://urlebird.com/search/videos/?q=skin+tag+remover", wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)
        
        html = await page.content()
        with open('ub_vid.txt', 'w', encoding='utf-8') as f:
            f.write(html)
        
        await browser.close()
asyncio.run(test_ub())
