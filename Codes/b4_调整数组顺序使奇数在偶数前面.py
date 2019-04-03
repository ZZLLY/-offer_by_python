class Solution:
    # 我的解法
    # def reOrderArray(self, array):
    #     for i in range(len(array)):
    #         flag = 0
    #         if array[i]%2 == 0:
    #             for j in range(i, len(array)):
    #                 if array[j]%2 == 1:
    #                     flag = 1
    #                     break
    #             if not flag:
    #                 break
    #             for k in range(j, i, -1):
    #                 array[k], array[k-1] = array[k-1], array[k]
    #     return array

    # 类似快排
    def reOrderArray(self, array):
        if len(array) <= 1:
            return array
        p = -1
        for i in range(len(array)):
            if array[i]%2 == 1:
                p += 1
                t = i
                tmp = array[t]
                while p < t:
                    array[t] = array[t-1]
                    t -= 1
                array[p] = tmp
        return array




s = Solution()
print(s.reOrderArray([1,2,3,4,5,6]))