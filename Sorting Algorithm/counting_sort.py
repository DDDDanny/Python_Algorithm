# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 0:16
# @Author  : DannyDong
# @File    : counting_sort.py
# @describe: 计数排序


class CountingSort(object):
    def __init__(self, arr=None):
        self.arr = arr

    def sort_asc(self):
        if self.arr is None:
            return False
        max_num = max(self.arr)
        min_num = min(self.arr)
        length = max_num - min_num + 1
        temp_arr = []

        for i in range(length):
            temp_arr.append(0)

        for i in self.arr:
            temp_arr[i-min_num] += 1

        for i in range(1, length):
            temp_arr[i] += temp_arr[i-1]

        res_arr = [0] * len(self.arr)

        for i in range(len(self.arr)-1, -1, -1):
            res_arr[temp_arr[self.arr[i]-min_num]-1] = self.arr[i]
            temp_arr[self.arr[i] - min_num] -= 1
        print(res_arr)


if __name__ == '__main__':
    arr_list = [1, 3, 8, 2, 7, 6, 5, 4]
    num_list = CountingSort(arr_list)
    num_list.sort_asc()
