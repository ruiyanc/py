import re
import urllib.request
import requests
import pyquery


headers = {
    # 知乎登录后的cookie
    'Cookie': '_zap=49cfc400-f328-4183-b50b-67860958e020;\
     _xsrf=cbb93eb7-2975-4b30-ba77-633d92113b4f; \
     d_c0="AMCjxGOOAQ-PTh2KYz3Sp1c8jdMp6zm4gf8=|1550582473";\
      ISSW=1; l_n_c=1; q_c1=3ae819bc0f4b4c4c8b0e67db16a96164|1554295205000|1554295205000;\
       n_c=1; tgw_l7_route=80f350dcd7c650b07bd7b485fcab5bf7; \
       l_cap_id="YzkzZTgzZjJlYjZiNDBjM2FhODI2MzQ1NDM0YjgzZWU=|1554297459|df6267fcffd54ff3dabff641ef9772448a80d806";\
        r_cap_id="MTgyYzU4MWJhZThhNDBjNWJjYWExYzY3ODgwMDY1NTA=|1554297459|242b9ed08f25acc5173030dcf30fe0002b3fcd74";\
         cap_id="NmEyZDc1ZGU3NjZhNGJmZTgwNmU4YzJkZjE0MzllOGE=|1554297459|d6024d454dc748a2953bf5625cd731267000fdca"; \
         capsion_ticket="2|1:0|10:1554297465|14:capsion_ticket|44:MWIyYmE3YWY1ODY0NDc1ZGI1NWE4ZGE0NjE2ZTE2ODY\
         =|8e535f4ff53a5e843c74368c08735f0f1187af8fb416dbce86f792a91e59800a"; \
         z_c0="2|1:0|10:1554297478|4:z_c0|92:Mi4xdUg4akF3QUFBQUFBd0tQRVk0NEJEeVlBQUFCZ0FsVk5oUUNTWFFBVExvODh\
         Cdk9LZnZIOWNydkFxb2NnaFRjZWh3|889b048d1d4d3c09543fca24226285e9891d43d04dcd33311a099d17bc0a7038"',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/73.0.3683.86 Safari/537.36',
    'Host': 'www.zhihu.com'
}
# r = requests.get('https://www.zhihu.com', headers=headers)
url = 'https://www.zhihu.com/explore'
html = requests.get(url, headers=headers).text
doc = pyquery.PyQuery(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pyquery.PyQuery(item.find('.content').html()).text()
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()
# print(r.text)
# print(r.status_code)
