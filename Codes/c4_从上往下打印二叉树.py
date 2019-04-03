# class Solution:
#     def PrintFromTopToBottom(self, root):
#         if not root:
#             return []
#         tmp = [root]
#         tmp2 = []
#         res = []
#         while tmp:
#             for node in tmp:
#                 res.append(node.val)
#                 if node.left:
#                     tmp2.append(node.left)
#                 if node.right:
#                     tmp2.append(node.right)
#             tmp = tmp2
#             tmp2 = []
#         return res

# 层次遍历, 用一个队列即可
class Solution:
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res