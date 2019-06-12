# by luffycity.com
import time

# time.sleep(2)  # 程序走到这儿会等待2s钟

# time模块主要是用来和时间打交道的
# 时间格式
    # '2018-8-20' '2018.8.20' 字符串数据类型     格式化时间 - 给人看的
    # 结构化时间
    # 1534732642.617272  浮点型数据类型,以s为单位 时间戳时间 - 给机器计算用的
    # 1970 1 1 0:0:0

# 时间戳时间
# print(time.time())

# 格式化时间
# print(time.strftime('%Y-%m-%d %H:%M:%S')) # str format time
# print(time.strftime('%y-%m-%d %H:%M:%S')) # str format time
# print(time.strftime('%c'))

# 结构化时间
# struct_time = time.localtime()  # 北京时间
# print(struct_time)
# print(struct_time.tm_mon)

# 时间戳换成字符串时间
# print(time.time())
# struct_time = time.localtime(1500000000)
# # print(time.gmtime(1500000000))
# ret = time.strftime('%y-%m-%d %H:%M:%S',struct_time)
# print(ret)

# 字符串时间 转 时间戳
# struct_time = time.strptime('2018-8-8','%Y-%m-%d')
# print(struct_time)
# res = time.mktime(struct_time)
# print(res)

# 1.查看一下2000000000时间戳时间表示的年月日
# 时间戳 - 结构化 - 格式化
# struct_t = time.localtime(2000000000)
# print(struct_t)
# print(time.strftime('%y-%m-%d',struct_t))

# 2.将2008-8-8转换成时间戳时间
# t = time.strptime('2008-8-8','%Y-%m-%d')
# print(time.mktime(t))

# 3.请将当前时间的当前月1号的时间戳时间取出来 - 函数
# 2018-8-1
# def get_time():
#     st = time.localtime()
#     st2 = time.strptime('%s-%s-1'%(st.tm_year,st.tm_mon),'%Y-%m-%d')
#     return time.mktime(st2)
# print(get_time())

# 4.计算时间差 - 函数
    # 2018-8-19 22:10:8 2018-8-20 11:07:3
    # 经过了多少时分秒
# str_time1 = '2018-8-19 22:10:8'
# str_time2 = '2018-8-20 11:07:3'
# struct_t1 = time.strptime(str_time1,'%Y-%m-%d %H:%M:%S')
# struct_t2 = time.strptime(str_time2,'%Y-%m-%d %H:%M:%S')
# timestamp1 = time.mktime(struct_t1)
# timestamp2 = time.mktime(struct_t2)
# sub_time = timestamp2 - timestamp1
# gm_time = time.gmtime(sub_time)
# # 1970-1-1 00:00:00
# print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(gm_time.tm_year-1970,gm_time.tm_mon-1,
#                                  gm_time.tm_mday-1,gm_time.tm_hour,
#                                  gm_time.tm_min,gm_time.tm_sec))

