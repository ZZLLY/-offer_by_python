# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# # 这样做虽然ac了,但是是有问题的
# def get_list(root):
#     node = root
#     stack = [node]
#     res = []
#     while len(stack) > 0:
#         res.append(node.val)
#         if node.right is not None:
#             stack.append(node.right)
#         if node.left is not None:
#             stack.append(node.left)
#         node = stack.pop()
#     return res
#
#
# class Solution:
#     def HasSubtree(self, pRoot1, pRoot2):
#         # write code here
#         if not pRoot1 or not pRoot2:
#             return False
#         # 先序遍历两个树, 转化成查找子串
#         tree1 = get_list(pRoot1)
#         tree2 = get_list(pRoot2)
#
#         for i in range(len(tree1)):
#             if tree2 == tree1[i:i+len(tree2)]:
#                 return True
#         return False

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        res = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                res = self.DoesTree1haveTree2(pRoot1, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.left, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.right, pRoot2)
        return res

    def DoesTree1haveTree2(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1haveTree2(pRoot1.left, pRoot2.left) \
                and self.DoesTree1haveTree2(pRoot1.right, pRoot2.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
s = Solution()
print(s.HasSubtree(root, root))

