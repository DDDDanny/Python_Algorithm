# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 21:50
# @Author  : DannyDong
# @File    : insertion_sort.py
# @describe: 插入排序


class InsertionSort(object):
    # 初始化
    def __init__(self, arr=None):
        self.arr = arr

    # 升序
    def sort_asc(self):
        if self.arr is None:
            return None
        cnt = len(self.arr)
        for i in range(1, cnt):
            # 存当前位置的值
            cur_num = self.arr[i]
            # 当前位置前一个的索引
            pre_index = i - 1
            # 当前值与它之前的每一个值进行比较，直到满足不了循环条件
            while pre_index >= 0 and cur_num < self.arr[pre_index]:
                self.arr[pre_index + 1] = self.arr[pre_index]
                pre_index -= 1
            self.arr[pre_index + 1] = cur_num
        print(self.arr)

    # 降序
    def sort_desc(self):
        if self.arr is None:
            return None
        cnt = len(self.arr)
        for i in range(1, cnt):
            cur_num = self.arr[i]
            pre_index = i - 1
            while pre_index >= 0 and cur_num > self.arr[pre_index]:
                self.arr[pre_index + 1] = self.arr[pre_index]
                pre_index -= 1
            self.arr[pre_index + 1] = cur_num
        print(self.arr)


if __name__ == '__main__':
    arr_list = [1, 3, 8, 2, 7, 6, 5, 4]
    num_list = InsertionSort(arr_list)
    num_list.sort_asc()
    num_list.sort_desc()
