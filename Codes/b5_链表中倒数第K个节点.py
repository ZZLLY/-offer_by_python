# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 解法1：
    # 用数组存, 在返回第-k个节点
    # def FindKthToTail(self, head, k):
    #     tmp = []
    #     p = head
    #     while p:
    #         tmp.append(p)
    #         p = p.next
    #     if len(tmp) < k or k < 1:
    #         return
    #     return tmp[-k]

    # 解法2：
    # 指针1和2从第一个节点开始
    # 让指针1跑到k个节点, 然后指针1和2一起出发, 直到指针1到末位节点
    def FindKthToTail(self, head, k):
        if not head or k<1:
            return
        p = head
        q = head
        for i in range(k-1):
            if p.next:
                p = p.next
            else:
                # 说明k大于链表长度
                return
        while p.next:
            p = p.next
            q = q.next
        return q
