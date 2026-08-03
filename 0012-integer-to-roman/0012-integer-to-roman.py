class Solution(object):
    def intToRoman(self, num):
        result=""
        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        for i in range(len(value)):
            while num>=value[i]:
                result+=symbols[i]
                num=num-value[i]
        return result
        