# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 21:17
# @Author  : DannyDong
# @File    : shell_sort.py
# @describe: 希尔排序


class ShellSort(object):
    # 初始化
    def __init__(self, arr=None):
        self.arr = arr

    # 升序
    def sort_asc(self):
        if self.arr is None:
            return False
        # 间隔标识
        flag = len(self.arr) // 2
        while flag > 0:
            for i in range(flag, len(self.arr)):
                index = i
                cur_num = self.arr[i]
                while index - flag >= 0 and cur_num < self.arr[index - flag]:
                    self.arr[index] = self.arr[index - flag]
                    index -= flag
                self.arr[index] = cur_num
            flag //= 2
        print(self.arr)

    # 升序
    def sort_desc(self):
        if self.arr is None:
            return False
        # 间隔标识
        flag = len(self.arr) // 2
        while flag > 0:
            for i in range(flag, len(self.arr)):
                index = i
                cur_num = self.arr[i]
                while index - flag >= 0 and cur_num > self.arr[index - flag]:
                    self.arr[index] = self.arr[index - flag]
                    index -= flag
                self.arr[index] = cur_num
            flag //= 2
        print(self.arr)


if __name__ == '__main__':
    arr_list = [1, 3, 8, 2, 7, 6, 5, 4]
    num_list = ShellSort(arr_list)
    num_list.sort_asc()
    num_list.sort_desc()

"""
One:
    flag = 4
    
    1, 3, 8, 2      1, 3, 5, 2
                =>              => [1, 3, 5, 2, 7, 6, 8, 4]
    7, 6, 5, 4      7, 6, 8, 4

Two:
    flag = 2
    
    1, 3      1, 2
    
    5, 2      5, 3
          =>        => [1, 2, 5, 3, 7, 4, 8, 6]
    7, 6      7, 4

    8, 4      8, 6

Three:
    flag = 1
    
    [1, 2, 3, 4, 5, 6, 7, 8]
"""