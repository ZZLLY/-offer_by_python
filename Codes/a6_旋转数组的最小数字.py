class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        # 比较, 如果发生旋转, 必然有一个数比前一个数小
        for i in range(1, len(rotateArray)):
            if rotateArray[i] < rotateArray[i-1]:
                return rotateArray[i]
        # 没发生旋转
        return rotateArray[0]