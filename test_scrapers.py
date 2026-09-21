import asyncio
import json
import urllib.request
import urllib.parse
from playwright.async_api import async_playwright

async def test_meta(keyword):
    print("Testing Meta...")
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
        page = await browser.new_page()
        
        encoded = urllib.parse.quote(keyword)
        url = f"https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q={encoded}&search_type=keyword_unordered"
        print(f"Navigating to {url}")
        
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_timeout(5000)
        
        # take screenshot to see what's happening
        await page.screenshot(path="meta_debug.png")
        
        # let's just grab all text
        text = await page.evaluate("document.body.innerText")
        print(f"Meta Page text snippet: {text[:500]}")
        
        await browser.close()

async def test_tiktok_api(keyword):
    print("Testing TikWM API...")
    url = f"https://tikwm.com/api/feed/search?keywords={urllib.parse.quote(keyword)}&count=5"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            print("TikWM API Response keys:", data.keys())
            if 'data' in data and 'videos' in data['data']:
                videos = data['data']['videos']
                print(f"Found {len(videos)} videos from TikWM API")
                if videos:
                    v = videos[0]
                    print(f"Sample: ID {v.get('video_id')} URL {v.get('play')}")
    except Exception as e:
        print(f"TikWM API failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_meta("skin tag remover"))
    asyncio.run(test_tiktok_api("skin tag remover"))
