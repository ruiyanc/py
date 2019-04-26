import re
import urllib.request
import requests

data = {
    'name': 'tom',
    'age': 22
}
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
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)
# r = requests.get("https://github.com/favicon.ico", headers=headers)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)
'''
r = requests.post("http://httpbin.org/post", data=data, headers=headers)
print(r.status_code)
print(r.headers)
print(r.cookies)
print(r.url)
print(r.history)
'''
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post("http://httpbin.org/post", files=files)
# print(r.text)