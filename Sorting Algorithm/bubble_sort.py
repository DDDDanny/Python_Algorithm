# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 15:12
# @Author  : DannyDong
# @File    : bubble_sort.py
# @describe: 冒泡排序


class BubbleSort(object):
    # 初始化
    def __init__(self, arr=None):
        self.arr = arr

    # 升序
    def sort_asc(self):
        if self.arr is None:
            return False
        # 统计长度
        cnt = len(self.arr)
        for i in range(cnt - 1):
            for j in range(cnt - 1 - i):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        print(self.arr)

    # 降序
    def sort_desc(self):
        if self.arr is None:
            return False
        # 统计长度
        cnt = len(self.arr)
        for i in range(cnt - 1):
            for j in range(cnt - 1 - i):
                if self.arr[j] < self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        print(self.arr)


if __name__ == '__main__':
    arr_list = [1, 3, 8, 2, 7, 6, 5, 4]
    num_list = BubbleSort(arr_list)
    num_list.sort_asc()
    num_list.sort_desc()
