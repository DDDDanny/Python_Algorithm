# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:00
# @Author  : DannyDong
# @File    : double_linked_list.py
# @describe: 双向循环链表


# 节点类
class Node(object):
    def __init__(self, data=None, pre_node=None, next_node=None):
        self.data = data
        self.pre_node = pre_node
        self.next_node = next_node


# 链表实现类
class DoubleLinkList(object):
    # 初始化
    def __init__(self):
        node = Node()
        node.pre_node = node
        node.next_node = node
        self.head = node
        self.length = 0

    # 获取链表长度
    def __len__(self):
        return self.length

    # head.data 为空，第一个节点是head后的第一个节点
    def first_node(self):
        return self.head.next_node

    # 后去最后一个节点
    def end_node(self):
        return self.head.pre_node

    # 从链表末尾添加节点
    def end_append(self, data):
        node = Node(data)
        end_node = self.end_node()
        end_node.next_node = node
        node.pre_node = end_node
        node.next_node = self.head
        self.head.pre_node = node
        self.length += 1

    # 从链表head添加节点
    def start_append(self, data):
        node = Node(data)
        first_node = self.first_node()
        self.head.next_node = node
        node.pre_node = self.head
        node.next_node = first_node
        first_node.pre_node = node
        self.length += 1

    # 返回每个节点
    def iter_node(self):
        cur_node = self.first_node()
        if cur_node is self.head:
            return -1
        while cur_node.next_node is not self.head:
            yield cur_node
            cur_node = cur_node.next_node
        yield cur_node

    # 从链表任意位置添加(按位置添加，添加后位置会变)
    def insert(self, data, index):
        node = Node(data)
        # index_i类似索引
        index_i = 1
        if self.length < index:
            raise Exception('out of range')
        if self.head.next_node is self.head:
            self.end_append(data)
            return True
        else:
            if index == 0:
                self.start_append(data)
                return True
            else:
                for cur_node in self.iter_node():
                    if index_i == index:
                        temp_node = cur_node.next_node
                        node.pre_node = cur_node
                        cur_node.next_node = node
                        node.next_node = temp_node
                        temp_node.pre_node = node
                        self.length += 1
                        return True
                    index_i += 1

    # 删除链表中任意位置的节点(按位置删除，删除后位置会变)
    def del_node(self, index):
        # index_i类似索引
        index_i = 1
        if self.length < index:
            raise Exception('out of range')
        for cur_node in self.iter_node():
            if index_i == index:
                temp_next_node = cur_node.next_node
                temp_pre_node = cur_node.pre_node
                temp_pre_node.next_node = temp_next_node
                temp_next_node.pre_node = temp_pre_node
                del cur_node
                self.length -= 1
                return True
            index_i += 1


# 测试数据
if __name__ == '__main__':
    link_list = DoubleLinkList()
    link_list.end_append(5)
    link_list.end_append(6)
    link_list.start_append(2)
    link_list.start_append(1)
    link_list.insert(3, 2)
    link_list.insert(4, 3)
    link_list.del_node(1)
    link_list.del_node(3)
    link_list.del_node(6)

    print(len(link_list))
