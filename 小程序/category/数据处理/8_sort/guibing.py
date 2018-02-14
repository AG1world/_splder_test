def merge_sort(li):
    n = len(li)

    # 当列表长度为1，则表示该列表为有序列表，直接返回，用于合并
    if 1 == n:
        return li

    mid = n // 2
    # 拆分左侧列表
    left_sorted_li = merge_sort(li[:mid])
    # return merge_sort(li[:mid])

    # 拆分右侧列表
    right_sorted_li = merge_sort(li[mid:])

if __name__ == '__main__':
    # li = [12, 34, 77, 43, 23, 89, 21, 35, 67]
    li = [1, 3, 2,4]
    sorted_li = merge_sort(li)
    # print(sorted_li)