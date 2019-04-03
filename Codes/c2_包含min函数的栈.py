# 最小栈
# 用一个辅助栈
# 压入数时记录降序序列
# 弹出时判断是否与辅助栈顶的数相同, 相同则一并弹出
# 举例：顺序压入7 4 3 5 2 6 8 9
# 辅助栈里: 7 4 3 2
# min函数返回辅助栈顶
class Solution:
    def __init__(self):
        self.stack = []
        self.p = []
    def push(self, node):
        self.stack.append(node)
        if self.p == [] or node<=self.p[-1]:
            self.p.append(node)
    def pop(self):
        if not self.stack:
            return None
        res = self.stack.pop()
        if self.p[-1] == res:
            self.p.pop()
        return res
    def top(self):
        return self.stack[-1] if self.stack else None
    def min(self):
        return self.p[-1] if self.p else None