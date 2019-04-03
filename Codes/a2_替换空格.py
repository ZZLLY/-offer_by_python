class Solution:
    # 我的解法:
    # 用str.replace
    # tip: str.replace(old=' ', new='%20')会报错
    # 原因在于此方法使用c语言写的, 不支持python的keyword参数特性
    # def replaceSpace(self, s):
    #     return s.replace(' ', '%20')

    # 如果不用内置函数
    def replaceSpace(self, s):
        return '%20'.join(s.split(' '))


s = Solution()
print(s.replaceSpace('We Are Happy'))
