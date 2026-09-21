import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True)
        page = await b.new_page()
        try:
            print("Connecting to TikTok...")
            await page.goto('https://www.tiktok.com/search?q=skin%20tag%20remover', timeout=10000)
            print("Success")
        except Exception as e:
            print(f"Failed: {e}")
        await b.close()

asyncio.run(test())
