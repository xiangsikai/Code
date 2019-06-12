# by luffycity.com
import os


class ExistsError(Exception):
    pass

class KeyInvalidError(Exception):
    pass

def new_func(path,prev):
    """
    去path路径的文件中，找到前缀为prev的一行数据，获取数据并返回给调用者。
        1000,成功
        1001,文件不存在
        1002,关键字为空
        1003,未知错误
        ...
    :return:
    """
    response = {'code':1000,'data':None}
    try:
        if not os.path.exists(path):
            raise ExistsError()

        if not prev:
            raise KeyInvalidError()
        pass
    except ExistsError as e:
        response['code'] = 1001
        response['data'] = '文件不存在'
    except KeyInvalidError as e:
        response['code'] = 1002
        response['data'] = '关键字为空'
    except Exception as e:
        response['code'] = 1003
        response['data'] = '未知错误'
    return response


def func(path,prev):
    """
    去path路径的文件中，找到前缀为prev的一行数据，获取数据并返回给调用者。
        1000,成功
        1001,文件不存在
        1002,关键字为空
        1003,未知错误
        ...
    :return:
    """
    response = {'code':1000,'data':None}
    try:
        if not os.path.exists(path):
            response['code'] = 1001
            response['data'] = '文件不存在'
            return response
        if not prev:
            response['code'] = 1002
            response['data'] = '关键字为空'
            return response
        pass
    except Exception as e:
        response['code'] = 1003
        response['data'] = '未知错误'
    return response

def show():
    return 8


def run():
    pass