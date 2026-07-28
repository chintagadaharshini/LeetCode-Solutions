class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        a1={}
        a2={}
        for ch in s:
            if ch in a1:
                a1[ch]+=1
            else:
                    a1[ch]=1
        for ch in t:
            if ch in a2:
                a2[ch]+=1
            else:
                    a2[ch]=1
        return a1==a2

