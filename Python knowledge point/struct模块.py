import struct


res=struct.pack("i","")

print(res)
print(len(res))


obj=struct.unpack("i",res)
print(obj[0])
