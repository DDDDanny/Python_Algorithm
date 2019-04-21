# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 17:35
# @Author  : DannyDong
# @File    : merge_sort.py
# @describe: 归并排序


class MergeSort(object):
    def __init__(self, sort_type='asc'):
        self.sort_type = sort_type

    # 排序基础方法
    def sort_base(self, left_list=None, right_list=None):
        res = []
        # 升序
        if self.sort_type == 'asc':
            while len(left_list) > 0 and len(right_list) > 0:
                if left_list[0] < right_list[0]:
                    res.append(left_list.pop(0))
                else:
                    res.append(right_list.pop(0))
        # 降序
        elif self.sort_type == 'desc':
            while len(left_list) > 0 and len(right_list) > 0:
                if left_list[0] > right_list[0]:
                    res.append(left_list.pop(0))
                else:
                    res.append(right_list.pop(0))
        else:
            raise Exception('Parameter error! sort_type is asc or desc! ')

        res += left_list
        res += right_list
        return res

    # 递归实现排序
    def sort_asc(self, arr=None):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_list, right_list = arr[:mid], arr[mid:]
        return self.sort_base(self.sort_asc(left_list), self.sort_asc(right_list))


if __name__ == '__main__':
    arr_list = [1, 3, 8, 2, 7, 6, 5, 4]
    # sort_type = 'asc'为升序  sort_type = 'desc'为降序
    num_list = MergeSort('asc')
    print(num_list.sort_asc(arr_list))
