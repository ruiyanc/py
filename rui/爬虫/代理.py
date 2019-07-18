import requests
from selenium import webdriver

proxies = {
    'http': 'http://35.197.112.156:3128',
    'https': 'https://119.180.142.125:8060',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/73.0.3683.86 Safari/537.36'
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies, headers=headers)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://127.0.0.1:8118')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')
