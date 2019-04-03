class Solution:
    def jumpFloorII(self, number):
        tmp = [0, 1, 2]
        while len(tmp) <= number:
            # 距离一步 + 距离两步 + ... + 距离n步
            tmp.append(sum(tmp)+1)
        return tmp[number]