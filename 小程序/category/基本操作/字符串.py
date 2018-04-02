# sorted(student.items(), key=lambda v: v[1])
# 字符串的长度进行排列
lst = ['a2222','bsb', 'eee']
new_list = list(map(lambda x:x[1],sorted(list(map(lambda x:(len(x),x),lst)))))
print(new_list)
# 1.得出列表的每个元素的长度,对长度值排列
# 2. 对排列的每个长度对应的值返回一个新列表




l = sorted(list(map(lambda x:(len(x),x),lst)))

l2 = list(map(lambda x:x[1],l))

print(l2)
# 最简单方式
lst.sort(key=lambda x:len(x))
print(lst)

# d = list(map(sorted(),l))
# print(l)