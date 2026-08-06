class Solution(object):
    def brokenCalc(self, startValue, target):
        moves=0
        while target>startValue:
            if target%2==0:
                target/=2
            else:
                target+=1
            moves+=1
        return moves+(startValue-target)