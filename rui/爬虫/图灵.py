import re
import itchat
import requests


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing', 'Picture'])
def text_reply(msg):
    # 判断发件人是不是自己
    if not msg['FormUserName'] == Name["言睿"]:
        url = "http://www.tuling123.com/openapi/api?key=e4393409d9724892b2e35d27e5fca0d9&info="
        # 将获取的信息附在链接的尾部
        url = url + msg['Text']
        html = getHtmlText(url)
        message = re.findall(r'\"text\":\".*?\"', html)
        reply = eval(message[0].split(':')[1])
        return reply


if __name__ == '__main__':
    # 通过itchat扫码登录微信网页版
    itchat.auto_login()
    # 获取所有微信好友的信息
    friends = itchat.get_friends(update=True)[0:]
    Name = {}
    Nic = []
    User = []
    for i in range(len(friends)):
        Nic.append(friends[i]["NickName"])
        User.append(friends[i]["UserName"])
    for i in range(len(friends)):
        Name[Nic[i]] = User[i]
    itchat.run()
