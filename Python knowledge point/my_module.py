# by luffycity.com
# __all__ = ['name','read1','read2']
__all__ = ['name']

print(12345)

name = 'alex'

def read1():
    print('hello world')

def read2():
    print('in read1 func',name)

print(54321)

if __name__ == '__main__':
    print(__name__)  # "__main__"
    print([__name__])