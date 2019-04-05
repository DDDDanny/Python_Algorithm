# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 21:22
# @Author  : DannyDong
# @File    : linked_list.py
# @describe: 单链表练习


# 节点类
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


# 链表结构类
class LinkList(object):
    def __init__(self):
        # 初始化链表头节点及长度
        self.head = Node()
        self.length = 0

    def __len__(self):
        return self.length

    # 从链表末尾添加节点
    def end_append(self, data):
        node = Node(data)
        # 如果链表长度为0，添加的节点为第一个节点
        if self.length == 0:
            self.head.next_node = node
            self.length += 1
            return True
        else:
            cur_node = self.head
            # while一直找到最后一个节点，将新节点添加至最后一节点的后面
            while cur_node.next_node is not None:
                cur_node = cur_node.next_node
            cur_node.next_node = node
            self.length += 1
            return True

    # 从链表开始添加节点
    def start_append(self, data):
        node = Node(data)
        if self.length == 0:
            self.head.next_node = node
            self.length += 1
            return True
        else:
            temp = self.head.next_node
            self.head.next_node = node
            node.next_node = temp
            self.length += 1
            return True

    # 生成器函数，会把每一个节点返回
    def iter_node(self):
        if self.length == 0:
            raise Exception('length error')
        cur_node = self.head.next_node
        # while 和 if 的位置不能换，否则最后一个节点会被省掉
        while cur_node.next_node is not None:
            yield cur_node
            cur_node = cur_node.next_node
        if cur_node.next_node is None:
            yield cur_node

    # 在任意位置插入节点
    def insert(self, location, data):
        node = Node(data)
        if self.length == 0:
            self.head.next_node = node
            self.length += 1
            return True
        else:
            for index in self.iter_node():
                if index.data == location:
                    temp = index.next_node
                    index.next_node = node
                    node.next_node = temp
                    self.length += 1
                    return True

    # 删除任意节点
    def del_node(self, data):
        if self.length == 0:
            raise Exception('length error')
        else:
            per_node = self.head
            for cur_node in self.iter_node():
                if cur_node.data == data:
                    per_node.next_node = cur_node.next_node
                    del cur_node
                    self.length -= 1
                    return True
                else:
                    per_node = cur_node

    # 更新节点
    def update_node(self, old_node, new_node):
        if self.length == 0:
            raise Exception('length error')
        else:
            for cur_node in self.iter_node():
                if cur_node.data == old_node:
                    cur_node.data = new_node
                    return True


if __name__ == '__main__':
    link_list = LinkList()
    link_list.end_append(1)
    link_list.end_append(2)
    link_list.end_append(3)
    link_list.start_append(4)
    link_list.start_append(5)
    link_list.start_append(6)
    link_list.insert(1, 7)
    link_list.insert(2, 8)
    link_list.insert(3, 9)
    link_list.del_node(1)
    link_list.del_node(2)
    link_list.del_node(1)
    link_list.update_node(1, 7)
    link_list.update_node(2, 8)
    link_list.update_node(3, 9)

    print('链表长度：', len(link_list))
