import time
import urllib.request
import http.cookiejar
from urllib.robotparser import RobotFileParser

data = {
    'name': 'germey',
}
# response = urllib.request.urlopen('http://www.apache.org')
# print(response.read().decode('utf-8'))
# print(response.getheader('Server'))

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# for item in cookie:
#     print(item.name + " = " + item.value)

# rp = RobotFileParser('http://www.jianshu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('*', 'http://www.jianshu.com/p'))
# print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python'))
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/73.0.3683.86 Safari/537.36'
}
# r = requests.get('https://www.zhihu.com/explore')

# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post("http://httpbin.org/post", headers=headers, files=files)
# print(r.text)

# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + " " + value)

# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456")
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

proxies = {
    'http': 'http://127.0.0.1:8118',
    'https': 'https://127.0.0.1:8118',
}
# r = requests.get('https://www.taobao.com', proxies=proxies)
# r = requests.get('http://localhost:5000', auth=('username', 'password'))
# url = "http://httpbin.org/post"
# s = requests.Session()
# req = requests.Request('POST', url, data=data, headers=headers)
# prepped = s.prepare_request(req)
# r = s.send(prepped)

# print(r.text)
# print(r.status_code)

# from lxml import etree
# html = etree.parse('x.html', etree.HTMLParser())
# print(html.xpath('//*'))
from bs4 import BeautifulSoup
# import pyquery
# print(pyquery.PyQuery(url='https://cuiqingcai.com')('title'))

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.jd.com')
# lis = browser.find_elements('.service-bd li')
input = browser.find_element_by_id('key')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('button')
button.click()
print(browser.current_url)
print(browser.page_source)
# print(lis)
# print(browser.page_source)
browser.close()