class Solution:
    # 递归超时
    # def jumpFloor(self, number):
    #     if number <= 2:
    #         return number
    #     return self.jumpFloor(number-1) + self.jumpFloor(number-2)
    #

    def jumpFloor(self, number):
        tmp = [0, 1, 2]
        for i in range(number-1):
            # 距离一步 + 距离两步
            tmp.append(tmp[-1] + tmp[-2])
        return tmp[number]