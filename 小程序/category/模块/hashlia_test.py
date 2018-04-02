# 哈希算法加密
# 对于同一内容获取定长的数据,单项加密


import hashlib

h  = hashlib.md5('iojoij'.encode('utf-8'))  # 生成对象的时候是加盐

h.update('hello'.encode('utf8'))
print(h.hexdigest())    # 对象对字符串打加密, 5d41402abc4b2a76b9719d911017c592


h.update('world'.encode('utf8'))
print(h.hexdigest())   # e8b8e41ac1beca4a664f77237f3bf04b
                        # 将会得到上面与下面加密字符串拼接打值