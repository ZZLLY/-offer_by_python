# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 我的解法:
    # 先顺序遍历,保存在list里,然后反向输出
    # def printListFromTailToHead(self, listNode):
    #     tmp = []
    #     p = listNode
    #     while p:
    #         tmp.append(p.val)
    #         p = p.next
    #     return tmp[::-1]

    # 用递归实现
    def printListFromTailToHead(self, listNode):
        if listNode:
            return self.printListFromTailToHead(listNode.next) + [listNode.val]
        else:
            return []

