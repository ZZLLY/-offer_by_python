class Solution:
    def Mirror(self, root):
        if not root:
            return
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node.left, node.right = node.right, node.left
        return root

