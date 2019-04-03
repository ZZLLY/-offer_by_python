# class Solution:
#     def VerifySquenceOfBST(self, sequence):
#         # 先找到根节点, 后序遍历根节点一定在最后
#         if not sequence:
#             return False
#         root = sequence[-1]
#         flag = 0
#         index = len(sequence)-1
#         for i, item in enumerate(sequence):
#             if not flag and item > root:
#                 flag = 1
#                 index = i
#             if flag and item < root:
#                 return False
#         if sequence[:index]:
#             left = self.VerifySquenceOfBST(sequence[:index])
#         else:
#             left = True
#         if sequence[index:-1]:
#             right = self.VerifySquenceOfBST(sequence[index:-1])
#         else:
#             right = True
#         return left and right

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        size = len(sequence)-1
        while size:
            i = 0
            while sequence[i] < sequence[size]:
                i += 1
            while sequence[i] > sequence[size]:
                i += 1
            if i < size:
                return False
            size -= 1
        return True

s = Solution()
print(s.VerifySquenceOfBST([2,4,3,6,8,7,5]))