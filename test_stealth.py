import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        res = stealth(page)
        if asyncio.iscoroutine(res):
            await res
        print("Success!")
        await browser.close()

asyncio.run(test())
