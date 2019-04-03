# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # pHead 始终指向要反转的结点
    # last 指向反转后的首结点
    # 每反转一个结点，把pHead结点的下一个结点指向last, last指向pHead成为反转后首结点, 再把pHead向前移动一个结点直至None结束
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last