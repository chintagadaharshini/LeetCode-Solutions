class Solution(object):
    def hammingWeight(self, n):
        count=0
        binary=bin(n)
        for digit in binary:
            if digit=='1':
                count+=1
        return count
