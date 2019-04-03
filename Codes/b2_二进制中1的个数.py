class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            # 补码表示
            n = n & 0xffffffff
        while n:
            count += n & 1
            n = n>>1
        return count

s = Solution()
print(s.NumberOf1(-1))