class Solution:
    # 偷懒
    # def Power(self, base, exponent):
    #     return base**exponent

    # 快速幂
    def Power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        res = 1
        e = abs(exponent)
        tmp = base
        while e:
            if e&1 == 1:
                res = res*tmp
            e = e>>1
            tmp = tmp * tmp
        return res if exponent>0 else 1/res

s = Solution()
print(s.Power(2,5))