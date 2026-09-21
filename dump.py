import asyncio
from playwright.async_api import async_playwright
async def t():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True)
        page=await browser.new_page()
        await page.goto('https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=skin%20tag%20remover&search_type=keyword_unordered')
        await page.wait_for_timeout(3000)
        html=await page.content()
        open('meta_html.txt','w',encoding='utf-8').write(html)
        await browser.close()
asyncio.run(t())
