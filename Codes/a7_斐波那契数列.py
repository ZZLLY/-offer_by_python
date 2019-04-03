class Solution:
    # 递归超时
    # def Fibonacci(self, n):
    #     if n == 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     else:
    #         return self.Fibonacci(n-1) + self.Fibonacci(n-2)

    # 非递归
    def Fibonacci(self, n):
        tmp = [0, 1]
        # 循环n-1次, 每次加上前两个数之和
        for i in range(n-1):
            tmp.append(tmp[-1]+tmp[-2])
        return tmp[n]

    # def Fibonacci(self, n):
    #     tmp = [0] * (n+1)
    #     # 循环n-1次, 每次加上前两个数之和
    #     for i in range(n+1):
    #         if i <= 1:
    #             tmp[i] = i
    #         else:
    #             tmp[i] = tmp[i-1] + tmp[i-2]
    #     return tmp[n]