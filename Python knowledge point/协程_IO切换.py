from gevent import monkey
monkey.patch_all() # 以后代码中遇到IO都会自动执行greenlet的switch进行切换
import requests
import gevent


def get_page1(url):
    ret = requests.get(url)
    print(url,ret.content)

def get_page2(url):
    ret = requests.get(url)
    print(url,ret.content)

def get_page3(url):
    ret = requests.get(url)
    print(url,ret.content)

gevent.joinall([
    gevent.spawn(get_page1, 'https://www.python.org/'), # 协程1
    gevent.spawn(get_page2, 'https://www.yahoo.com/'),  # 协程2
    gevent.spawn(get_page3, 'https://github.com/'),     # 协程3
])