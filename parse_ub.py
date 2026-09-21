import re
html = open('ub_vid.html', encoding='utf-8').read()
matches = re.findall(r'https?://[^\s\"\']+\.mp4[^\s\"\']*', html)
print(matches)

matches2 = re.findall(r'https?://[^\s\"\']+video[^\s\"\']*', html)
print([m for m in matches2 if 'urlebird.com/video/' not in m])
