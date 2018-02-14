
# 选择排序
# 思想:通过待排序列中找到最大值,并将最大值放在排序序列的起始位置
#      当待排序中左边元素大于最大值,就将左边元素给到max(最大值下标)


def select_sort(li):
    '选择排序,以max为基准'
    n =len(li)
    # 外循环将进行n-1 次
    for i in range(n-1): # 1,2,8,7,5,6 //   n-2,n-1,
        #内循环,每次选择一个最大值,当左侧出现比预定max大时,就将此值的下标付给max,
        # 内循环结束后,当默认max值下标不与标记j值相等,就将li[j]赋值给
        max_index = n-1-i

        for j in range(max_index-1,-1,-1):
            # 当
            if li[j] >li[max_index]:
                max_index = j

        if max_index !=n-1-i :
            li[max_index],li[n-i-1] = li[n-i-1],li[max_index]

def select_sort_min(li):
    n = len(li)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if li[j]<li[min_index]:
                min_index = j
        # 当原定min_index = i
        if min_index !=i:
            li[i],li[min_index] = li[min_index],li[i]




if __name__ =='__main__':
    li = [4, 9, 1, 11, 45, 8, 34]
    select_sort(li)
    print(li)
    print('--------------')
    select_sort_min(li)
    print(li)
