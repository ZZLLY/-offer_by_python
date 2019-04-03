# # AC了  但是嫌写法繁琐
class Solution:
    def printMatrix(self, matrix):
        if not matrix:
            return
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        row = len(matrix)
        col = len(matrix[0])
        start = [0, -1]
        res = []
        index = 0
        for i in range(row*col):
            for j in range(index, index+4):
                item = direction[j%4]
                now = [start[0] + item[0], start[1] + item[1]]
                if 0 <= now[0] < row and 0 <= now[1] < col:
                    if matrix[now[0]][now[1]] != '#':
                        res.append(matrix[now[0]][now[1]])
                        matrix[now[0]][now[1]] = '#'
                        start = now
                        index = j%4
                        break
        return res


s = Solution()
print(s.printMatrix([[1,2],[3,4]]))

