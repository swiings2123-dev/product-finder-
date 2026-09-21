import json
from bs4 import BeautifulSoup

def find_keys(d, target, result):
    if isinstance(d, dict):
        for k, v in d.items():
            if k == target:
                result.append(v)
            else:
                find_keys(v, target, result)
    elif isinstance(d, list):
        for i in d:
            find_keys(i, target, result)

def test():
    with open('meta_html.txt', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    scripts = soup.find_all('script', type='application/json')
    
    snapshots = []
    for s in scripts:
        try:
            data = json.loads(s.string)
            find_keys(data, 'snapshot', snapshots)
        except:
            pass
            
    print(f"Found {len(snapshots)} snapshots")
    if snapshots:
        print(snapshots[0].get('body', {}).get('text', '')[:100])
        if snapshots[0].get('videos'):
            print("Video URL:", snapshots[0]['videos'][0].get('video_hd_url') or snapshots[0]['videos'][0].get('video_sd_url'))
            
test()
