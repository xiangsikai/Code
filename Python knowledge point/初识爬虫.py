# by luffycity.com
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor


# 模拟浏览器发送请求
# 内部创建 sk = socket.socket()
# 和抽屉进行socket连接 sk.connect(...)
# sk.sendall('...')
# sk.recv(...)

def task(url):
    print(url)
    r1 = requests.get(
        url=url,
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        }
    )

    # 查看下载下来的文本信息
    soup = BeautifulSoup(r1.text,'html.parser')
    print(soup.text)
    # content_list = soup.find('div',attrs={'id':'content-list'})
    # for item in content_list.find_all('div',attrs={'class':'item'}):
    #     title = item.find('a').text.strip()
    #     target_url = item.find('a').get('href')
    #     print(title,target_url)

def run():
    pool = ThreadPoolExecutor(5)
    for i in range(1,50):
        pool.submit(task,'https://dig.chouti.com/all/hot/recent/%s' %i)


if __name__ == '__main__':
    run()