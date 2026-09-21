import re
html = open('ub_vid.html', encoding='utf-8').read()
matches = re.findall(r'https?://[^\s\"\']+', html)
videos = [m for m in matches if '.mp4' in m or 'video' in m]
for v in set(videos):
    if 'urlebird' not in v:
        print(v)
