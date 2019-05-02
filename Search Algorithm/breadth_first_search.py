# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 21:23
# @Author  : DannyDong
# @File    : breadth_first_search.py
# @describe: 广度优先搜索

import queue


def bfs(data, start):
    # 初始化集合，存放已经访问过的节点（无序不重复元素序列）
    visited = set()
    # 初始化队列
    q = queue.Queue()
    # 将开始值写入队列
    q.put(start)
    while not q.empty():
        # 获取队列值，并移除
        num = q.get()
        print(num)
        # 返回指定键的值
        for v in data.get(num, []):
            if v not in visited:
                visited.add(v)
                q.put(v)


if __name__ == '__main__':
    graph = {1: [2, 3], 2: [4, 5], 3: [6]}
    bfs(graph, 1)
