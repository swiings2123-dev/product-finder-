from duckduckgo_search import DDGS
import json

def test():
    keyword = "skin tag remover"
    query = f'site:youtube.com/shorts/ "{keyword}"'
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=5))
        for r in results:
            print(r['title'], r['href'])

test()
