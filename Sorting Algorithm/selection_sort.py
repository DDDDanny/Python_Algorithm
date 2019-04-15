# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 22:08
# @Author  : DannyDong
# @File    : selection_sort.py
# @describe: 选择排序


class SelectionSort(object):
    # 初始化
    def __init__(self, arr=None):
        self.arr = arr

    # 升序
    def sort_asc(self):
        if self.arr is None:
            return False
        cnt = len(self.arr)
        for i in range(cnt - 1):
            min_index = i
            for j in range(i + 1, cnt):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        print(self.arr)

    # 降序
    def sort_desc(self):
        if self.arr is None:
            return False
        cnt = len(self.arr)
        for i in range(cnt - 1):
            max_index = i
            for j in range(i + 1, cnt):
                if self.arr[j] > self.arr[max_index]:
                    max_index = j
            self.arr[i], self.arr[max_index] = self.arr[max_index], self.arr[i]
        print(self.arr)


if __name__ == '__main__':
    arr_list = [1, 3, 8, 2, 7, 6, 5, 4]
    num_list = SelectionSort(arr_list)
    num_list.sort_asc()
    num_list.sort_desc()
