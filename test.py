import re
html=open('ub.txt', encoding='utf-8').read()
matches=re.findall(r'src=[\'"]([^\'"]+)[\'"]', html)
print(matches[:5])
