class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # append从后开始放
        self.stack1.append(node)

    def pop(self):
        if not self.stack2:
            # 把第一个栈的数全部弹出给第二个栈
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()