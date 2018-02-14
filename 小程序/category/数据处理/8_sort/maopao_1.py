# 冒泡排序
# 思想:
# 1.俩俩相邻的元素进行比较,右为大,每一轮比较都会将max值沉到最大位置,
# 2.就不需进行下一轮的比较,每次循环之后就会未排序列表长度就-1
# 3.慢慢的从大往小,逐一替换,就像冒泡一样

def maopao(li):
    '冒泡排序'
    # [1, 2, 3, 4, 5, 6, 7]   1,2 2,3 3,4 4,5 5,6 6,7
    n = len(li)
    # 列表交换完成需要n-1次
    for i in range(n-1):
        # 每次循环后都会出现一个max值,即循环i次就出现i次max值
        for j in range(n-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]

if __name__ =='__main__':
    li = [4, 9, 1, 11, 45, 8, 34]
    maopao(li)
    print(li)