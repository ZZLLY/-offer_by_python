# -*- conding:utf-8 -*-
# 思路：用一个辅助栈模拟弹出情况
# 如果辅助栈顶的元素和popV[j], 及时弹出这个数, 并且j+1
# 最后如果辅助栈为空, 说明成功模拟出弹出情况
class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV:
            return
        stack = []
        j = 0
        for i in range(len(pushV)):
            stack.append(pushV[i])
            while j < len(popV) and stack[-1] == popV[j]:
                stack.pop()
                j += 1
        return len(stack) == 0

s = Solution()
s.IsPopOrder([1,2,3,4,5],[4,3,5,1,2])