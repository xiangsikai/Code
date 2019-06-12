# by luffycity.com
import threading



# #################### 1. 计算密集型多线程无用 ####################
# v1 = [11,22,33] # +1
# v2 = [44,55,66] # 100
#
#
# def func(data,plus):
#     for i in range(len(data)):
#         data[i] = data[i] + plus
#
# t1 = threading.Thread(target=func,args=(v1,1))
# t1.start()
#
# t2 = threading.Thread(target=func,args=(v2,100))
# t2.start()


# #################### 2. IO操作 多线程有用 ####################
# import threading
# import requests
# import uuid
#
# url_list = [
#     'https://www3.autoimg.cn/newsdfs/g28/M05/F9/98/120x90_0_autohomecar__ChsEnluQmUmARAhAAAFES6mpmTM281.jpg',
#     'https://www2.autoimg.cn/newsdfs/g28/M09/FC/06/120x90_0_autohomecar__ChcCR1uQlD6AT4P3AAGRMJX7834274.jpg',
#     'https://www2.autoimg.cn/newsdfs/g3/M00/C6/A9/120x90_0_autohomecar__ChsEkVuPsdqAQz3zAAEYvWuAspI061.jpg',
# ]
#
# def task(url):
#     ret = requests.get(url)
#     file_name = str(uuid.uuid4()) + '.jpg'
#     with open(file_name, mode='wb') as f:
#         f.write(ret.content)
#
# for url in url_list:
#
#     t = threading.Thread(target=task,args=(url,))
#     t.start()