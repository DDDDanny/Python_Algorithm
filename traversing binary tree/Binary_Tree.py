# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 22:10
# @Author  : DannyDong
# @File    : Binary_Tree.py
# @describe: 遍历二叉树（先序、中序、后序和层级遍历）


# 二叉树节点及树的生成类
class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 实现二叉树遍历
class Traversing(object):
    def __init__(self):
        # 初始化队列
        self.tree_queue = []
        # 初始化节点数量
        self.node_num = 0
        # 树的深度
        self.depth = 0

    # 先序遍历
    def prev_order(self, binary_tree=None):
        if binary_tree is None:
            return False
        print(binary_tree.data)
        self.prev_order(binary_tree.left)
        self.prev_order(binary_tree.right)

    # 中序遍历
    def mid_order(self, binary_tree=None):
        if binary_tree is None:
            return False
        self.mid_order(binary_tree.left)
        print(binary_tree.data)
        self.mid_order(binary_tree.right)

    # 后序遍历
    def over_order(self, binary_tree=None):
        if binary_tree is None:
            return False
        self.over_order(binary_tree.left)
        self.over_order(binary_tree.right)
        print(binary_tree.data)

    # 层次遍历(队列)
    def level_traversal(self, binary_tree=None):
        if binary_tree is None:
            return False
        node = binary_tree
        self.tree_queue.append(node)
        while self.tree_queue:
            self.node_num += 1
            node = self.tree_queue.pop(0)
            print(node.data)
            if node.left is not None:
                self.tree_queue.append(node.left)
            if node.right is not None:
                self.tree_queue.append(node.right)
        print('节点数量：', self.node_num)


if __name__ == '__main__':
    # 实例化对象
    tree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))
    bt = Traversing()
    print('先序遍历')
    bt.prev_order(tree)
    print('中序遍历')
    bt.mid_order(tree)
    print('后序遍历')
    bt.over_order(tree)
    print('层次遍历')
    bt.level_traversal(tree)

"""
         A
       /   \
      B     C
     / \   / \
    D   E F   G
"""