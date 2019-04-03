class Solution:
    def rectCover(self, number):
        tmp = [0, 1, 2]
        while len(tmp) <= number:
            tmp.append(tmp[-1] + tmp[-2])
        return tmp[number]