class Solution:
    # 两种方法：
    # 1. 把每一行当做有序数组, 进行二分查找 nlog(n)
    # def Find(self, target, array):
    #     for row in array:
    #         low = 0
    #         high = len(row)-1
    #         while low <= high:
    #             mid = (low+high)//2
    #             if row[mid] < target:
    #                 low = mid + 1
    #             elif row[mid] > target:
    #                 high = mid - 1
    #             else:
    #                 return True
    #     return False

    # 2. 根据规律, 从数组左下角出发
    # 如果target比now大, 右移一位
    # 反之, 上移一位 n
    def Find(self, target, array):
        x = len(array)-1
        y = 0
        while x >= 0 and y <= len(array[0])-1:
            if target > array[x][y]:
                y += 1
            elif target < array[x][y]:
                x -= 1
            else:
                return True
        return False


s = Solution()
a = [[1, 2, 4], [2, 3, 5], [4, 5, 6]]
print(s.Find(3, a))



