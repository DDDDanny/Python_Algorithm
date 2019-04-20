# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 22:47
# @Author  : DannyDong
# @File    : quick_sort.py
# @describe: 快速排序


class QuickSort(object):
    def __init__(self):
        pass

    # 升序
    def sort_asc(self, arr=None):
        if len(arr) <= 1:
            return arr
        key = arr[0]

        min_list, max_list = [], []
        for i in arr[1:]:
            if i < key:
                min_list.append(i)
            else:
                max_list.append(i)
        res = self.sort_asc(min_list) + [key] + self.sort_asc(max_list)
        return res

    # 降序
    def sort_desc(self, arr=None):
        if len(arr) <= 1:
            return arr
        key = arr[0]

        # python的魅力所在
        min_list = [i for i in arr[1:] if i < key]
        max_list = [i for i in arr[1:] if i >= key]
        return self.sort_desc(max_list) + [key] + self.sort_desc(min_list)


if __name__ == '__main__':
    arr_list = [1, 3, 8, 2, 7, 6, 5, 4]
    num_list = QuickSort()
    print(num_list.sort_asc(arr_list))
    print(num_list.sort_desc(arr_list))
