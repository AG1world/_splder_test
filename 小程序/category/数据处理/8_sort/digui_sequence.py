# -*- coding:utf-8 -*-



# 实现递归执行后的代码,是等待递归全部完成
# 还是压栈后栈顶的第一个代码后,执行递归代码之后
#　答案是在获取栈顶结果后就执行下面的程序，在返回第二层或者栈顶并排任务



def digui_test(li):
    if len(li) == 1:
        return li
    count = 0
    mid = len(li) // 2
    # print('mid',mid)
    # 拆分列表获取左侧单个列表
    result_l = digui_test(li[:mid])
    # print('--------------',result_l)
    # 拆分列表获取右侧单个列表
    result_r = digui_test(li[mid:])
    # print('>>>>>>>>>>',result_r)
    print('----LEFT-------', result_l)
    print('>>>>RIGHT>>>', result_r)
    # 合并liebiao ,以插入的形式
    # 1.初始化游标,新列表
    left = 0
    right = 0
    new_sorted_list = []
    # 2.合并列表,当小的就按照顺序添加到new_sort_list 中
    # 列表的长度是游标的遍历接线
    left_n = len(result_l)
    right_n = len(result_r)
    while left < left_n and right < right_n:
        if result_l[left] <= result_r[right]:
            # 等于浩保证,左边相等的元素会优先取到左边去
           new_sorted_list.append(result_l[left])
           left +=1
        else:
            new_sorted_list.append(result_r[right])
            right += 1
    # new_sorted_list.append(result_l[left:])
    # new_sorted_list.append(result_l[right:])
    new_sorted_list += result_l[left:]
    new_sorted_list += result_r[right:]
    # append()是将item走位元素添加到列表中,+= 是将item作为列表与原列表拼接
    # demo: [1,2] += [] 得到还是原列表,而append()是添加一个[]元素
    print(new_sorted_list)
    return new_sorted_list
if __name__ == '__main__':
    li = [54, 26, 93, 17]
    digui_test(li)


# 第一次传入 mid = 2 ,
# result_l = func(li[0:2]);result_r = func(li[2:0])

# 第二次 result_l = func(li[0:2])  获得mid =1
# result_l = func(li[0:1]);result_r = func(li[1:0])
# 第二次 左边地一层 获得 [54],[26]

# 第三次   result_r = func(li[2:0]) 获得mid = 1
# result_l = func(li[0:1]);result_r = func(li[1:0])
# 第二次 左边地一层 获得 [93],[17]

"""
----LEFT------- [54]
>>>>RIGHT>>> [26]
[26, 54]

----LEFT------- [93]
>>>>RIGHT>>> [17]
[17, 93]

----LEFT------- [26, 54]
>>>>RIGHT>>> [17, 93]
[17, 26, 54, 93]
递归函数return就像一个
"""
