# 验证递归函数中return作用

# 一个列表 li = [1, 4, a, b, 7],递归得到的列表将是数字将添加[],
# 字fuchuan添加{},切以自身为key值,对应的下标为value值

# 重新定义生成一个is_num()函数用来测试是否为数字
import unicodedata

def isnumber(i):
    '生成测试是否为数字的函数,真为True,假为False'
    try:
        # 若为数字必可以转化称浮点型
        float(i)
        return True
    except:
        return False
    try:
        unicodedata.numeric(i)
        return True
    except:
        return False
def is_string(i):
    try:
        i.isalpha()
        return True
    except:
        return False

# 循环获取
def decoraty(li):
    '将列表中元素转化称列表或者字典'

    if not len(li):
        return '请输入正确的列表形式'
    new_li = []

    for n,i in enumerate(li):
        # 判断是否为数字
        if isnumber(i):
            new_li.append([i])
        # 判断是否为字符串
        elif is_string(i):
            new_li.append({i:n})
        else:
            new_li.append(i)

    return new_li
li = [1, 4, 'a', 'b', 7,[1]]
l1 = decoraty(li)


# 递归
"""
n =10

n-0 = 10 -0
n-1 = 10 +　10-1
n-2 = 10 + 10-1 + 10-2
n-3 = 10 + 10-1 + 10-2+ 10-3


n-9 = 10 + 10-1 + ... 10-9
n-10 = 10 + 10-1 + ... 10-9 + 10-10

"""
def recursion(n):
    if n ==0 :
        return 0
    result = n + recursion(n-1)
    count = 0
    count += result
    print(count)
    # recursion(n-1)
    return count
if __name__ == '__main__':
    recursion(10)
    print(recursion(10))
# n = 3
"""
n = 3
result = recursion(2) + recursion(1)
result = recursion(1)+recursion(0) + recursion(1) + recursion(0)


"""