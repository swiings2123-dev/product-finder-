import re
from bs4 import BeautifulSoup

html = open('ub_vid2.html', encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')

scripts = soup.find_all('script')
for s in scripts:
    if s.string and 'mp4' in s.string:
        print("Found mp4 in script!")
        print(s.string[:200])

for s in scripts:
    if s.string and 'video' in s.string:
        print("Found video in script!")
        print(s.string[:200])
