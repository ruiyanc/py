from requests import Session
from db import RedisQueue
from request import WeixinRequest
from urllib.parse import urlencode


class Spider():
    base_url = 'http://weixin.sogou.com/weixin'
    keyword = 'NBA'
    headers = {
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Encoding': 'gzip',
        'Accept': 'text/html,application/xhtml+xml,application/xml;\
                q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'SMYUV=1556302359983345;ABTEST=2|1560665246|v1;IPLOC=CN4201;SUID=ADB93971771A910A000000005D05DC9E;\
                SUID=ADB939712F20910A000000005D05DCA5;weixinIndexVisited=1;sct=1;SNUID=C9DC5D156461EE0FD7DF3DEE65B24370;JSESSIONID=aaaMCpeCkX1I86hi_hiRw',
        'Host': 'weixin.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/74.0.3729.108 Safari/537.36',
    }
    session = Session()
    queue = RedisQueue()

    def start(self):
        """
        初始化工作
        :return:
        """
        # 全局更新Headers
        self.session.headers.update(self.headers)
        start_url = self.base_url + '?' + urlencode(
            {'query': self.keyword, 'type': 2}
        )
        weixin_request = WeixinRequest(url=start_url, callback=self.parse_index, need_proxy=True)
        # 调度第一个请求
        self.queue.add(weixin_request)