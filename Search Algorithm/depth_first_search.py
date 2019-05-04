# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 18:26
# @Author  : DannyDong
# @File    : depth_first_search.py
# @describe: 深度优先搜索


def dfs(data, start):
    # 初始化集合，存放已经访问过的节点（无序不重复元素序列）
    visited = set()
    # 初始化二维list，模拟栈。第一个值记录当前字典中的键，第二个值记录键对应list的索引
    stack = [[start, 0]]
    print(start)
    # 当list为空，表示图遍历完成
    while stack:
        # stack[-1]指的是list最后一个元素
        v, next_child_idx = stack[-1]
        if v not in data or next_child_idx >= len(data[v]):
            stack.pop()
            continue
        next_child = data[v][next_child_idx]
        stack[-1][1] += 1
        if next_child in visited:
            continue
        print(next_child)
        visited.add(next_child)
        stack.append([next_child, 0])


if __name__ == '__main__':
    data_dict = {1: [2, 3], 2: [4, 5], 3: [6]}
    dfs(data_dict, 1)
