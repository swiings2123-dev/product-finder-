import re
html = open('ub_vid.html', encoding='utf-8').read()
matches = re.findall(r'<a[^>]+href=[\'"]([^\'"]+)[\'"][^>]*>(.*?[Dd]ownload.*?)</a>', html, flags=re.DOTALL)
print([m[0] for m in matches])
