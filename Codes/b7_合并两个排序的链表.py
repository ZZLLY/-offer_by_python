# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_list(list):
    head = ListNode(0)
    p = head
    for i in list:
        tmp = ListNode(i)
        p.next = tmp
        p = p.next
    return head.next

class Solution:
    # 非递归, 新建了一条链表
    def Merge(self, pHead1, pHead2):
        head = ListNode(0)
        p = head
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                p.next = pHead1
                pHead1 = pHead1.next
            else:
                p.next = pHead2
                pHead2 = pHead2.next
            p = p.next
        if pHead1:
            p.next = pHead1
        else:
            p.next = pHead2
        return head.next

    # 递归
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val>pHead2.val:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2
        else:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1

s = Solution()
p = get_list([1, 4, 5])
q = get_list([2, 3, 6])
res = s.Merge(p, q)
while res:
    print(res.val, end=' ')
    res = res.next