from curl_cffi import requests
import re
r=requests.get('https://www-tiktok-com.translate.goog/@healthylifeguru/video/7407074347781033246?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp', impersonate='chrome120')
matches = re.findall(r'https?://[^\s\"\']+', r.text)
videos = set([m for m in matches if 'mp4' in m])
for v in videos:
    print(v)
